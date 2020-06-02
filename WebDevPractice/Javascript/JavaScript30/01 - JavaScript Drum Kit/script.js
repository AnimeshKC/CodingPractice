function playSound(e) {
  //get the audio and key of the element with the corresponding data-key
  const audio = document.querySelector(`audio[data-key="${e.keyCode}"]`);
  const keyElement = document.querySelector(`div[data-key="${e.keyCode}"]`);

  if (!audio) return; //end if the pressed key is not present in the document

  //add the playing class to the key pressed; this leads to a transition effect
  keyElement.classList.add("playing");

  //reset the audio each time a key is pressed, in the case of rapid presses
  audio.currentTime = 0;

  audio.play(); //play the corresponding audio
}

function removeTransition(e) {
  //remove the "playing" transition found in the "transform" property
  if (e.propertyName !== "transform") return;
  e.target.classList.remove("playing");
}
//Create an array containing all keys
const keys = document.querySelectorAll(".key");

//listen to the keys being pressed and play the sound
window.addEventListener("keydown", playSound);

for (let key of keys) {
  key.addEventListener("transitionend", removeTransition);
}
