// Importing Dictionary
var dict1_1 = {"一ねんせい": "いち",
"右にまがる": "みぎ",
"雨がふる": "あめ",
"ひゃく円がほしい": "えん",
"王さまはえらい": "おう",
"そとから音がする": "おと",
"下をみる": "した",
"火がついた": "ひ",
"花がさく": "はな",
"貝をひろう": "かい"
};

var dict1_2 = {"一": "いち",
"右": "みぎ",
"雨": "あめ",
"円": "えん",
"王": "おう",
"音": "おと",
"下": "した",
"火": "ひ",
"花": "はな",
"貝": "かい"
};

var dict2_1 = {"さんすうを学ぶ": "まな",
"てん気がわるい": "き",
"チョコが九こある": "きゅう",
"がっこうを休む": "やす",
"きん玉": "たま",
"金ようび": "きん",
"空をみあげる": "そら",
"月がでる": "つき",
"犬とさんぽする": "いぬ",
"ままのかおを見る": "み"
};

var dict2_2 = {"学ぶ": "まな",
"てん気": "き",
"九": "きゅう",
"休む": "やす",
"玉": "たま",
"金": "きん",
"空": "そら",
"月": "つき",
"犬": "いぬ",
"見る": "み"
};

var dict3_1 = {"口をひらく": "くち",
"がっ校にいく": "こう",
"左にまがる": "ひだり",
"チョコを三こもらう": "さん",
"山にのぼる": "やま",
"子どもがたくさんいる": "こ",
"チョコを四こもらう": "よん",
"糸でふくをぬう": "いと",
"けいは、むずかしい字をしっている": "じ",
"耳くそがたくさんとれた": "みみ"
};

var dict3_2 = {"口": "くち",
"校": "こう",
"左": "ひだり",
"三": "さん",
"山": "やま",
"子": "こ",
"四": "よん",
"糸": "いと",
"字": "じ",
"耳": "みみ"
};

var dict4_1 = {"七さいになった": "なな",
"車にのる": "くるま",
"手をあらう": "て",
"十じにねる": "じゅう",
"いえからそとに出る": "で",
"けいはすきな女のこがいる": "おんな",
"小さいさかなをかった": "ちい",
"上をむく": "うえ",
"森のなかからおとがする": "もり",
"たくさんの人がいる": "ひと"
};

var dict4_2 = {"七": "なな",
"車": "くるま",
"手": "て",
"十": "じゅう",
"出る": "で",
"女": "おんな",
"小さい": "ちい",
"上": "うえ",
"森": "もり",
"人": "ひと"
};

var dict5_1 = {"水をのむ": "みず",
"正しいことをする": "ただ",
"パパはながく生きる": "い",
"青いそら": "あお",
"夕がたにはいえにかえろう": "ゆう",
"石をなげる": "いし",
"赤いとんぼ": "あか",
"チョコを千こもらう": "せん",
"川でおぼれる": "かわ",
"えんぴつの先はとがっている": "さき"
};

var dict5_2 = {"水": "みず",
"正しい": "ただ",
"生きる": "い",
"青": "あお",
"夕": "ゆう",
"石": "いし",
"赤": "あか",
"千": "せん",
"川": "かわ",
"先": "さき"
};

// Default dict
var dictA = dict1_1

//making empty mistake_dict
var mistake_dict = {};

//initialize x
var x = 0;


// Creating buttons to select dictionary
var dict_button1_1 = d3.select("#button1_1");
var dict_button1_2 = d3.select("#button1_2");
var dict_button2_1 = d3.select("#button2_1");
var dict_button2_2 = d3.select("#button2_2");
var dict_button3_1 = d3.select("#button3_1");
var dict_button3_2 = d3.select("#button3_2");
var dict_button4_1 = d3.select("#button4_1");
var dict_button4_2 = d3.select("#button4_2");
var dict_button5_1 = d3.select("#button5_1");
var dict_button5_2 = d3.select("#button5_2");


// Making dictChange function
function dictChange(buttonSelected, dictSelected) {
  buttonSelected.on("click", function() {

    //Display or not display button
    document.getElementById("buttonA").style.display="";
    document.getElementById("buttonB").style.display="none";

    //empty mistake_dict
    mistake_dict = {};

    // Deleting mondai
    var mondaiForm = document.getElementById("mondai");
    mondaiForm.textContent = "";
    
    //setting new dict
    dictA = dictSelected
  
    //Reset x
    x = 0;
  
    // Showing new mondai
    d3.select("#mondai").text(Object.keys(dictA)[x])
  
    // Deleting answer in the form
    var resultForm = document.getElementById("textForm");
    resultForm.value = "";
  
    // Moving the cursor
    document.getElementById("textForm").focus();
  
    // Deleting comment
    var commentForm = document.getElementById("comment");
    commentForm.textContent = "";
  }) 
}

// Calling button and dictionary
dictChange(dict_button1_1, dict1_1)
dictChange(dict_button1_2, dict1_2)
dictChange(dict_button2_1, dict2_1)
dictChange(dict_button2_2, dict2_2)
dictChange(dict_button3_1, dict3_1)
dictChange(dict_button3_2, dict3_2)
dictChange(dict_button4_1, dict4_1)
dictChange(dict_button4_2, dict4_2)
dictChange(dict_button5_1, dict5_1)
dictChange(dict_button5_2, dict5_2)


//Showing the first mondai
d3.select("#mondai").text(Object.keys(dictA)[0])

//Display or not display button
document.getElementById("buttonA").style.display="";
document.getElementById("buttonB").style.display="none";


// Select buttonA
var submit = d3.select("#buttonA");



//making function when answer is submitted
submit.on("click", function() {

  // Prevent the page from refreshing
  d3.event.preventDefault();

  // Select the input element and get the raw HTML node
  var inputElement = d3.select("#textForm");

  // Get the value property of the input element
  var inputValue = inputElement.property("value");

  // Checking if the answer is correct or not
  if (inputValue == dictA[Object.keys(dictA)[x]]) {
    d3.select("#comment").text("せいかい！")
  } else {
    d3.select("#comment").text(`ざんねん！ せいかいは　「${dictA[Object.keys(dictA)[x]]}」`);
    mistake_dict[Object.keys(dictA)[x]] = dictA[Object.keys(dictA)[x]]
  }
  console.log(x)

  //Display or not display button
  document.getElementById("buttonA").style.display="none";
  document.getElementById("buttonB").style.display="";
  
})


// Select buttonB
var nextMondai = d3.select("#buttonB");




// giving function to buttonB to show next mondai
nextMondai.on("click", function() {

  if (x < Object.keys(dictA).length-1) { 
    // Adding 1 to x
    x += 1;
    
    // Showing new mondai
    d3.select("#mondai").text(Object.keys(dictA)[x])
    
    // Deleting answer in the form
    var resultForm = document.getElementById("textForm");
    resultForm.value = "";
    
    // Deleting comment
    var commentForm = document.getElementById("comment");
    commentForm.textContent = "";
    
    // Moving the cursor
    document.getElementById("textForm").focus();

    //Display or not display button
    document.getElementById("buttonA").style.display="";
    document.getElementById("buttonB").style.display="none";
  }

  else if (Object.keys(mistake_dict).length > 0) {

    // Deleting comment
    var commentForm = document.getElementById("comment");
    commentForm.textContent = "";

    d3.select("#comment").text(`${Object.keys(mistake_dict).length}つ まちがい まちがえたのをもういっかい`)

    //replace dictA with mistake_dict
    dictA = mistake_dict
    
    //empty mistake_dict
    mistake_dict = {};
    
    // Deleting mondai
    var mondaiForm = document.getElementById("mondai");
    mondaiForm.textContent = "";

    x = 0
   
    // Showing new mondai
    d3.select("#mondai").text(Object.keys(dictA)[x])

    // Deleting answer in the form
    var resultForm = document.getElementById("textForm");
    resultForm.value = "";

    // Moving the cursor
    document.getElementById("textForm").focus();

    //Display or not display button
    document.getElementById("buttonA").style.display="";
    document.getElementById("buttonB").style.display="none";

  }
  
  else{  
    // Final comment
    x = 0
    d3.select("#comment").text("やったね！おしまい！");
  }
});






  