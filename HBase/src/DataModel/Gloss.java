package DataModel;

import lombok.Getter;
import lombok.NonNull;
import lombok.RequiredArgsConstructor;
import lombok.Setter;

import javax.xml.namespace.QName;
import java.util.Iterator;

@RequiredArgsConstructor
public class Gloss {
    public static final QName TAG_NAME = new QName("gloss");

    @Getter
    @Setter
    @NonNull
    private String gloss;

    @Getter
    @Setter
    @NonNull
    private String lang;
}
