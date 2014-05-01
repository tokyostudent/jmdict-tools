///<reference path="./../Scripts/Promise.ts"/>
var WordSuggest;
(function (WordSuggest) {
    WordSuggest.defer = P.defer;
    WordSuggest.when = P.when;

    var Service = (function () {
        function Service() {
        }
        Service.prototype.lookup = function (str) {
            var d = WordSuggest.defer();
            d.resolve(new WordSuggest.Model("dsf"));

            return d.promise();
        };
        return Service;
    })();
    WordSuggest.Service = Service;
})(WordSuggest || (WordSuggest = {}));
//# sourceMappingURL=SuggestBoxService.js.map
