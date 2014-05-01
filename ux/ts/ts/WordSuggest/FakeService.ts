///<reference path="../Scripts/Promise.ts"/>


module WordSuggest {
    export class FakeService implements IService {
        _fakeEnglishResults:Array<Results.English> = [
            new Results.English("english1", "かないち", "漢字一")
        ];

        _fakeKanaResults: Array<Results.Kana> = [
                new Results.Kana()
        ];

        _fakeKanjiResults: Array<Results.Kanji> = [
            new Results.Kana()
        ];

        lookup(str: string): Promise<Model> {
            var retModel = new Model(
                this._fakeEnglishResults,
                this._fakeKanjiResults,
                this._fakeKanaResults);


            var d = defer<Model>();

            d.resolve(retModel);

            return d.promise();


        }
    }
}