function printError(elemId, hintMsg) {
  document.getElementById(elemId).innerHTML = hintMsg;
}

function validate() {
  let o1 = document.getElementById("option1").checked;
  let o2 = document.getElementById("option2").checked;



  if (o1 && !o2 || o2 && !o1) {
    printError("Err", "");
    return true;
  } else {
    printError("Err", "Пожалуйста, выберите один ответ.");
    return false;
  }
}

