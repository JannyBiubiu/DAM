var tpl = function (html, data) {
    return html.replace(/{{(\w+)}}/g, function (item, a, b) {
        return data[a];
    });
}
var wrap = function (html, data) {
    var result = '';
    for (var i = 0; i < data.length; i++) {
        result += tpl(html, data[i]);
    }
    return result;
}
fso = new ActiveXObject("Scripting.FileSystemObject");
var str = '<row>< col - md - 4 style= "border:groove;text-align:center" ><img src={{ filepath }} /><h2><a style="color:darkorange">{{ categories }}</a></h2></col - md - 4 ></row >';
document.getElementById('div').innerHTML = wrap(str, json);