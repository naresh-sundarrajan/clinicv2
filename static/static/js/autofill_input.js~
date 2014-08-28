/**This js is derived from example.js from typeahead library.
 *
 */

$(document).ready(function () {

    // read data from a csv file into a jason array.
    var data = csvJSON('/static/data/TestSamples.csv');

    // set up the data
    var medications = new Bloodhound({
        datumTokenizer: Bloodhound.tokenizers.obj.whitespace('value'),
        queryTokenizer: Bloodhound.tokenizers.whitespace,
        local: data
        //        prefetch: 'data/testsamples.json'
        //        remote: 'data/post_1960.json'
    });



    medications.initialize();
    medications.clearPrefetchCache();
    //    enable typeahead for <input> with id: custom-templates
    $('#custom-templates .typeahead').typeahead(null, {
        name: 'medications',
        displayKey: 'value',
        source: medications.ttAdapter(),
        //        set up the default text within the input
        templates: {
            empty: [
      '<div class="empty-message">',
      'unable to find any medications that match the current query',
      '</div>'
    ].join('\n'),
            //            Handlebars to render the drop-down menu's display format
            suggestion: Handlebars.compile('<div ><div style=\"display: inline-block; width:80%;\"><strong>{{aa}}</strong> ({{id}})</div> <div style=\"display: inline-block\">${{price}}</div></div><p>{{value}}</p>')
            //            suggestion: Handlebars.compile('<p><strong>{{aa}}</strong></p><p>{{value}}</p>')
        }
        //        trigger event on one option selected: show a editable template for detailed input (will be useful if input medications or radiology request)
    }).on("typeahead:selected",
        function (e, datum, name) {
            console.log(datum.id);
            console.log(datum.price);
            console.log(datum.aa);
            $('#custom-templates').append("<div id=\"detail\" style=\"display: inline-block;\"></div>");
            //            add elements for the template, the name is just for demo purpose, should be refined later
            $('#detail').append("<div>medication id: <input id = \"mid\" width=\"12\" align=\"right\" type = \"text\" value=\"" + datum.id + "\"></input >");
            $('#detail').append("<div>medication price: <input id = \"mprice\"  width=\"5\" align=\"right\" type = \"text\" value=\"" + datum.price + "\"></input >");
            //            switch the cursor focus in order
            $('#priminput').keydown(function (e) {
                if (e.which == 13) { // Enter
                    $('#mid').focus();
                } else if (e.which == 27) {
                    $('#detail').remove();
                }
            });
            $('#mid').keydown(function (e) {
                if (e.which == 13) { // Enter
                    $('#mprice').focus();
                }
            });
            //            clean up the template after final edit
            $('#mprice').keydown(function (e) {
                if (e.which == 13) { // Enter
                    $('#detail').remove();

                }
            });
        }
    );
});


function csvJSON(csvFile) {

    var csv = $.ajax({
        url: csvFile,
        async: false
    }).responseText;

    var lines = csv.split("\n");

    var result = [];

    var headers = lines[0].split(",");

    var length = headers.length;

    for (var i = 1; i < lines.length; i++) {

        var obj = {};
        var currentline = lines[i];
        var begin = 0;
        var end = 0;

        for (var j = 0; j < length; j++) {
            // causion: to deal with items contains "," and embraced by "
            if (currentline.substr(begin, 1) == "\"") {
                begin = begin + 1;
                end = currentline.indexOf("\"", begin);
            } else {
                end = currentline.indexOf(",", begin);
            }
            if (end > 0) {
                obj[headers[j]] = currentline.substring(begin, end);
            } else {
                obj[headers[j]] = currentline.substring(begin);
            }
            begin = end + 1;
            if (currentline.substr(begin, 1) == ",") {
                begin = begin + 1;
            }

        }
        result.push(obj);

    }
    a = JSON.stringify(result);
    //    console.log(a);
    return result;
}
