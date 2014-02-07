trait DictionaryQuery {
  def matches(s:String):Boolean
}

object DictionaryQuery {
  private class StartsWith(query:String) extends DictionaryQuery {
    val _query = query.toLowerCase

    def matches(s:String):Boolean = {
       _query.startsWith(s.toLowerCase)
    }
  }

  def apply(query:String):DictionaryQuery = {
    new StartsWith(query)
  }

}