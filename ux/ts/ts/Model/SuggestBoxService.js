///<reference path="./../Scripts/Promise.ts"/>
///<reference path="../WordSuggest/Model.ts"/>
define(["require", "exports"], function(require, exports) {
    exports.defer = P.defer;
    exports.when = P.when;

    var WordSuggest;
    (function (WordSuggest) {
        var SuggestBoxService = (function () {
            function SuggestBoxService() {
            }
            SuggestBoxService.prototype.lookup = function (str) {
                var d = exports.defer();
                d.resolve();

                return d.promise();
            };
            return SuggestBoxService;
        })();
        WordSuggest.SuggestBoxService = SuggestBoxService;
    })(WordSuggest || (WordSuggest = {}));
});
//# sourceMappingURL=SuggestBoxService.js.map
