///<reference path="./../Scripts/Promise.ts"/>



module WordSuggest {
    export class Service implements IService {
        _hara: WordSuggest.Model;

        public lookup(str: string): Promise<Model> {
            var d = defer<Model>();
            d.resolve(new Model(null, null, null));

            return d.promise();

        }
        
    }
} 