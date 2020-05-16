$(function(){
    var selectedItem = $(".numberTable_table tr").eq(0).children("td").eq(0);
    var numbers = [];   // 9 × 9　の配列
    for (var i = 0; i < 9; i++) {
        numbers[i] = [0,0,0,0,0,0,0,0,0];  
    }
    $(".numberTable_tableItem").on("click", function() {
        $(".numberTable_tableItem").css("background-color","#ffffff");
        $(this).css("background-color", "#8ec0e4");
        selectedItem = $(this);
    });

    $(".selectTable_tableItem").on("click", function() {
        if ( $(this).text() == "消" ) {
            selectedItem.css("color", "blue");
            selectedItem.text("");
            numbers[selectedItem.parents("tr").index()][selectedItem.index()] = 0;
        } 
        else {
            selectedItem.css("color", "black");
            selectedItem.text($(this).text());
            numbers[selectedItem.parents("tr").index()][selectedItem.index()] = parseInt($(this).text());
        }
    });

    $("#toku_button").on("click", function() {
        selectedItem.css("background-color", "#ffffff");
        selectedItem = $(".numberTable_table tr").eq(0).children("td").eq(0);
        $("#status").html("考え中・・・")
        json_numbers = JSON.stringify({"numbers" : numbers});
        $.ajax({
            type: "POST",
            url: "/kaidoku",
            data: json_numbers,
            contentType: "application/json",
            dataType: "json",
        })
        .done(function(data) {
            $("#status").html(data.result);
            for (var i = 0; i < 9; i++) {
                for (var j = 0; j < 9; j++) {
                    if (data.numbers[i][j] > 0) {
                        $(".numberTable_table tr").eq(i).children("td").eq(j).text(data.numbers[i][j]); 
                        numbers[i][j]  = data.numbers[i][j]
                    }
                }
            }
            // console.log(data.result);
            // console.log(data.numbers);
        })
        .fail( function(jqXHR, textStatus, errorThrown) {
            alert("失敗");
            console.log("textStatus  : " + textStatus);
            console.log("errorThrown : " + errorThrown.message);
        });
    });

    $("#clear_button").on("click", function() {
        for(var i = 0; i < 9; i++) {
            for (var j = 0; j < 9; j++) {
                myDOM= $(".numberTable_table tr").eq(i).children("td").eq(j);
                myDOM.text("");
                myDOM.css("color", "blue");
                myDOM.css("background-color", "#ffffff");
                numbers[i][j] = 0;
            }
        }
        $("#status").html("問題を入力してください。");
    });

    $("#sample_button").on("click", function() {
        var sample = [
            [8,0,0,0,0,0,0,0,0],
            [0,0,3,6,0,0,0,0,0],
            [0,7,0,0,9,0,2,0,0],
            [0,5,0,0,0,7,0,0,0],
            [0,0,0,0,4,5,7,0,0],
            [0,0,0,1,0,0,0,3,0],
            [0,0,1,0,0,0,0,6,8],
            [0,0,8,5,0,0,0,1,0],
            [0,9,0,0,0,0,4,0,0]
        ]; 
        for(var i = 0; i < 9; i++) {
            for (var j = 0; j < 9; j++) {
                numbers[i][j] = sample[i][j];
                var myDOM= $(".numberTable_table tr").eq(i).children("td").eq(j);
                myDOM.css("background-color", "#ffffff");
                if (sample[i][j] > 0) {
                    myDOM.css("color", "black");
                    myDOM.text(sample[i][j]);
                } else {
                    myDOM.css("color", "blue");
                    myDOM.text("");
                }
            }
        }
    });
});

