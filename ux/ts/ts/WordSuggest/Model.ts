///<reference path="../Scripts/Promise.ts"/>


module WordSuggest {
    export var defer = P.defer;
    export var when = P.when;
    export interface Promise<Value> extends P.Promise<Value> { }

    export module Results {
        export class English {
            constructor(public word: string,
                public kana: string,
                public kanji: string) {
                
            }
            }

        export class Kana {
            
        }

        export class Kanji {
            
        }
    }
    export class Model {
        constructor(
            public englishResults: Array<Results.English>,
            public kanaResults: Array<Results.Kana>,
            public kanjiResults: Array<Results.Kanji>)
        {
            

        }
    }
} 