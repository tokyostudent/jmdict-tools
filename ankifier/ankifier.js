///<reference path="node.d.ts"/>
var fs = require("fs");

if (3 != process.argv.length) {
    console.log("Need to provide the source file");
    process.exit();
}

var japFile = process.argv[2];

var japText = fs.readFileSync(japFile).toString("utf-8");
if (0 == japText.length) {
    console.log("Couldn't read from the jap file");
    process.exit();
}

var neededTranslations = japText.match(/^[a-zA-Z].*$/mg);

var PatternExecutor = (function () {
    function PatternExecutor(pattern, executor) {
        this.pattern = pattern;
        this.executor = executor;
    }
    PatternExecutor.prototype.executePattern = function (text) {
        var totalExecutions = 0;
        this.executor(this.pattern, text, function (translation) {
            totalExecutions++;

            var index = neededTranslations.indexOf(translation);

            neededTranslations.splice(index, 1);
        });

        return totalExecutions;
    };
    return PatternExecutor;
})();

function replace234Lines(r, text, counter) {
    text.replace(r, function (wholeMatch, kanji, reading, meaning) {
        console.log(kanji.trim() + "\t" + reading.trim() + "\t" + meaning.trim());
        counter(meaning);

        return "";
    });
}

var executors = [
    new PatternExecutor(/^$[\n\r]([^a-zA-Z\（\）]*)$[\n\r]([a-zA-Z].*)$/gm, function (r, text, counter) {
        text.replace(r, function (wholeMatch, reading, meaning) {
            console.log(reading.trim() + "\t", reading.trim() + "\t" + meaning.trim());
            counter(meaning);

            return "";
        });
    }),
    new PatternExecutor(/^$[\n\r]([^a-zA-Z]*)\（(.*)\）$[\n\r]([a-zA-Z].*)$/gm, replace234Lines),
    new PatternExecutor(/^$[\n\r]([^a-zA-Z]*)\（(.*)\）$[\n\r]^.*$[\n\r]([a-zA-Z].*)$/gm, replace234Lines),
    new PatternExecutor(/^$[\n\r]([^a-zA-Z]*)\（(.*)\）$[\n\r]^.*$[\n\r]^.*$[\n\r]([a-zA-Z].*)$/gm, replace234Lines)
];

var totalExecutions = 0;
for (var i = 0; i < executors.length; i++) {
    var currExecutor = executors[i];
    totalExecutions += currExecutor.executePattern(japText);
}

console.log("Made " + totalExecutions + " translations...");
if (0 != neededTranslations.length) {
    console.log("Still need to translate the following..., check your regexps");
    console.log(neededTranslations);
}

console.log("DO NOT FORGET TO ADD AN EMPTY LINE IN THE BEGINNING OF THE FILE");
console.log("ALSO SAVE THE WORDS FILE IN MAC FORMAT (will get to the conversion later)");
