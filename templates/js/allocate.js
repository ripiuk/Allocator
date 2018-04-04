var image_index = 0;
var image_list = {{images|safe}};
var image_list_length = image_list.length
var result = {};

function update_image_left(){
    document.getElementById('image_left').innerHTML = 'image '+ String(image_index + 1) + '/' + String(image_list_length);
};

window.onload = function(){
    update_image_left();
};

function open_modal(){
    document.getElementById("save").classList.add("is-active");
};

function close_modal(){
    document.getElementById("save").classList.remove("is-active");
};

function change_image(element){
    result[image_list[image_index]] = element.value;
    if (image_index >= (image_list_length - 1)){
      open_modal();
      return;
    };
    image_index++;
    document.getElementById("image_holder").src=image_list[image_index];
    update_image_left();
};

function save_result(){
    form = document.getElementById('save_form')

    for (key in result) {
      // alert('key: ' + key + ', value:' + result[key]); // debug
      var hiddenField = document.createElement("input");
      hiddenField.setAttribute("type", "hidden");
      hiddenField.setAttribute("name", key);
      hiddenField.setAttribute("value", result[key]);
      form.appendChild(hiddenField);
    }
    document.body.appendChild(form);
}