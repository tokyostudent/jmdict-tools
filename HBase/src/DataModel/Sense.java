package DataModel;

import lombok.Getter;

import javax.xml.namespace.QName;
import java.util.ArrayList;
import java.util.List;

public class Sense {
    public final static QName TAG_NAME = new QName("sense");
    public final static QName GLOSS_TAG_NAME = new QName("gloss");
    public final static QName STAGK_TAG_NAME = new QName("stagk");
    public final static QName STAGR_TAG_NAME = new QName("stagr");

    @Getter
    private List<Gloss> glossList = new ArrayList<Gloss>();

    @Getter
    private List<String> stagkList = new ArrayList<String>();

    @Getter
    private List<String> stagrList = new ArrayList<String>();

    public Boolean isSenseFor(KEle k_ele)
    {
        //if the sense does not have a stagk or stagr it's a sense for everything
        //otherwise k_ele must be in stagk

        if (getStagkList().isEmpty())
            return true;

        return getStagkList().contains(k_ele.getKeb());
    }

    public Boolean isSenseFor(REle r_ele)
    {
        //if the sense does not have a stagk or stagr it's a sense for everything
        //otherwise k_ele must be in stagk

        if (getStagkList().isEmpty())
            return true;

        return getStagkList().contains(r_ele.getReb());
    }




}
