module WordSuggest {

    export interface IService {
        lookup(str: string): Promise<Model>

    }
}