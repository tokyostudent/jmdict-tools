package DataModel;

import lombok.Getter;
import lombok.Setter;
import lombok.val;

import javax.xml.namespace.QName;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class Entry {
    public final static QName TAG_NAME = new QName("entry");

    @Getter
    @Setter
    private List<KEle> kEleList = new ArrayList<KEle>();

    @Getter
    @Setter
    private List<REle> rEleList = new ArrayList<REle>();

    @Getter
    @Setter
    private List<Sense> senseList = new ArrayList<Sense>();

    public List<REle> getRebs(KEle k_ele)
    {
        List<REle> retList = new LinkedList<REle>();

        for (REle r: getREleList())
            if (r.isReadingFor(k_ele))
                retList.add(r);

        return retList;
    }

    public List<Sense> getSenses(KEle k_ele, REle r_ele)
    {
        List<Sense> retSenses = new LinkedList<Sense>();

        for (Sense s: getSenseList())
            if (s.isSenseFor(k_ele) && s.isSenseFor(r_ele))
                retSenses.add(s);

        return retSenses;
    }

}
