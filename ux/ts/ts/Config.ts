///<reference path="./WordSuggest/IService.ts"/>
///<reference path="./WordSuggest/FakeService.ts"/>
///<reference path="./WordSuggest/Service.ts"/>


class AppConfig {
    private static _fakeService = new WordSuggest.FakeService();
    private static _realService = new WordSuggest.Service();

    public static wordSuggestService(useFake:boolean = false): WordSuggest.IService {
        return useFake ? AppConfig._fakeService : AppConfig._realService;
    }
} 