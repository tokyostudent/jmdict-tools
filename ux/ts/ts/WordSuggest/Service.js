///<reference path="./../Scripts/Promise.ts"/>
var WordSuggest;
(function (WordSuggest) {
    var Service = (function () {
        function Service() {
        }
        Service.prototype.lookup = function (str) {
            var d = WordSuggest.defer();
            d.resolve(new WordSuggest.Model(null, null, null));

            return d.promise();
        };
        return Service;
    })();
    WordSuggest.Service = Service;
})(WordSuggest || (WordSuggest = {}));
//# sourceMappingURL=Service.js.map
