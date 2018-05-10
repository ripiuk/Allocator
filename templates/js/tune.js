var class_num = 0;
var curr_num = 1;

function set_names(){
    class_num = parseInt(document.getElementById('classes').value);

    document.getElementById('rename_message').style.visibility = "visible";

    if (class_num < curr_num - 1){
      curr_num = 1;
      var myNode = document.getElementById("get_names");
      while (myNode.firstChild) {
          myNode.removeChild(myNode.firstChild);
      }
    };

    for (curr_num; curr_num <= class_num; curr_num++){
      var inp = document.createElement("INPUT");
      inp.name = curr_num;
      inp.value = curr_num;
      inp.classList.add("input");
      document.getElementById('get_names').appendChild(inp);
    }
    document.getElementById('save').style.visibility = "visible";
};