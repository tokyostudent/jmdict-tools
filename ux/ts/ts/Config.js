///<reference path="./WordSuggest/IService.ts"/>
///<reference path="./WordSuggest/FakeService.ts"/>
///<reference path="./WordSuggest/Service.ts"/>
var AppConfig = (function () {
    function AppConfig() {
    }
    AppConfig.wordSuggestService = function (useFake) {
        if (typeof useFake === "undefined") { useFake = false; }
        return useFake ? AppConfig._fakeService : AppConfig._realService;
    };
    AppConfig._fakeService = new WordSuggest.FakeService();
    AppConfig._realService = new WordSuggest.Service();
    return AppConfig;
})();
//# sourceMappingURL=Config.js.map
