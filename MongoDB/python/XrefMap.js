function XrefMap() {
    for (var i = 0; i < this.sense.length; i++) {
        if (!("xref" in this.sense[i]))
            continue;

        for (var j = 0; j < this.sense[i].xref.length; j++)
            if (this.sense[i].xref[j].indexOf("・") != -1)
                emit({ "__id": this._id, "senseIdx": i, "xrefIdx": j }, this.sense[i].xref[j]);
    }
}
