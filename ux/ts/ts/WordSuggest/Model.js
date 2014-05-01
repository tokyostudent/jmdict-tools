///<reference path="../Scripts/Promise.ts"/>
var WordSuggest;
(function (WordSuggest) {
    WordSuggest.defer = P.defer;
    WordSuggest.when = P.when;

    (function (Results) {
        var English = (function () {
            function English(word, kana, kanji) {
                this.word = word;
                this.kana = kana;
                this.kanji = kanji;
            }
            return English;
        })();
        Results.English = English;

        var Kana = (function () {
            function Kana() {
            }
            return Kana;
        })();
        Results.Kana = Kana;

        var Kanji = (function () {
            function Kanji() {
            }
            return Kanji;
        })();
        Results.Kanji = Kanji;
    })(WordSuggest.Results || (WordSuggest.Results = {}));
    var Results = WordSuggest.Results;
    var Model = (function () {
        function Model(englishResults, kanaResults, kanjiResults) {
            this.englishResults = englishResults;
            this.kanaResults = kanaResults;
            this.kanjiResults = kanjiResults;
        }
        return Model;
    })();
    WordSuggest.Model = Model;
})(WordSuggest || (WordSuggest = {}));
//# sourceMappingURL=Model.js.map
