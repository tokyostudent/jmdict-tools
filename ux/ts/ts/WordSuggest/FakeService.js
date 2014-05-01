///<reference path="../Scripts/Promise.ts"/>
var WordSuggest;
(function (WordSuggest) {
    var FakeService = (function () {
        function FakeService() {
            this._fakeEnglishResults = [
                new WordSuggest.Results.English("english1", "かないち", "漢字一")
            ];
            this._fakeKanaResults = [
                new WordSuggest.Results.Kana()
            ];
            this._fakeKanjiResults = [
                new WordSuggest.Results.Kana()
            ];
        }
        FakeService.prototype.lookup = function (str) {
            var retModel = new WordSuggest.Model(this._fakeEnglishResults, this._fakeKanjiResults, this._fakeKanaResults);

            var d = WordSuggest.defer();

            d.resolve(retModel);

            return d.promise();
        };
        return FakeService;
    })();
    WordSuggest.FakeService = FakeService;
})(WordSuggest || (WordSuggest = {}));
//# sourceMappingURL=FakeService.js.map
