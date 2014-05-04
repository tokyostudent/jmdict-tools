///<reference path="node.d.ts"/>


import fs = require("fs");


if (3 != process.argv.length)
{
	console.log("Need to provide the source file");
	process.exit();
}

var japFile = process.argv[2];


var japText = fs.readFileSync(japFile).toString("utf-8");
if (0 == japText.length)
{
	console.log("Couldn't read from the jap file");
	process.exit();
}


var neededTranslations = japText.match(/^[\d\(\)a-zA-Z].*$/mg);

class PatternExecutor {
	constructor(private pattern:RegExp, private executor: (r:RegExp, text:string, counter: (translation:string) => void) => void) {
		
	}

	executePattern(text:string): number {
		var totalExecutions:number = 0;
		this.executor(this.pattern, text, (translation:string) => {
				totalExecutions++;

				var index = neededTranslations.indexOf(translation);

				neededTranslations.splice(index, 1);
			});

		return totalExecutions;
	}
}

function replace234Lines(r:RegExp, text:string, counter: (translation:string) => void):void {
	text.replace(r, (wholeMatch, kanji, reading, meaning):string => {
        console.log(kanji.trim() + "\t" + reading.trim() + "\t" + meaning.trim());
		counter(meaning);

		return "";
		})
}

var executors:Array<PatternExecutor> = [
    new PatternExecutor(/^$[\n\r]([^a-zA-Z\（\）]*)$[\n\r]([\d\(\)a-zA-Z].*)$/gm, (r, text, counter: (translation:string) => void) => {
			text.replace(r, (wholeMatch, reading, meaning):string => {
                console.log(reading.trim() + "\t", reading.trim() + "\t" + meaning.trim());
				counter(meaning);

				return "";

				});
		}),

    new PatternExecutor(/^$[\n\r]([^a-zA-Z]*)\（(.*)\）$[\n\r]([\d\(\)a-zA-Z].*)$/gm, replace234Lines),
    new PatternExecutor(/^$[\n\r]([^a-zA-Z]*)\（(.*)\）$[\n\r]^.*$[\n\r]([\d\(\)a-zA-Z].*)$/gm, replace234Lines),
    new PatternExecutor(/^$[\n\r]([^a-zA-Z]*)\（(.*)\）$[\n\r]^.*$[\n\r]^.*$[\n\r]([\d\(\)a-zA-Z].*)$/gm, replace234Lines)
];


var totalExecutions:number = 0;
for (var i = 0; i < executors.length; i++)
{
	var currExecutor = executors[i];
	totalExecutions += currExecutor.executePattern(japText);
}

console.log("Made " + totalExecutions + " translations...");
if (0 != neededTranslations.length)
{
	console.log("Still need to translate the following..., check your regexps");
	console.log(neededTranslations);
}


console.log("DO NOT FORGET TO ADD AN EMPTY LINE IN THE BEGINNING OF THE FILE");
console.log("ALSO SAVE THE WORDS FILE IN MAC FORMAT (will get to the conversion later)");