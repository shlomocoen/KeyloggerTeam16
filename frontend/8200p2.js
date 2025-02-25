//  בקשת מידע מהשרת - מקבל את שמות המחשבים עליהם רצה ההאזנה
fetch("http://127.0.0.1:5000/api/get_target_machines_list").then(
    response => response.json()
    ).then(
        data => {
             // data מקבל את התוכן בתוך אובייקט למשתנה 
            console.log(data)
            const list = data.machines
            // ועוברים על השמות בלולאה listהרשימה עם המכונות עברה ל
            list.forEach(item => {
                // יוצר אלמנט קישור חדש עם קישור לדף הבא עם פרמטר כשם המכונה
                const new_element = document.createElement("a")
                new_element.href = `8200p3.html?computer=${item}`
                new_element.setAttribute('class', 'button1')
                new_element.textContent = item
                console.log(new_element)
                // יוצר אלמנט שורה חדש ומכניס לתוכו את הקישור המעוצב שנוצר 
                const new_p = document.createElement("p")
                new_p.appendChild(new_element)
                // ומכניס לתוכו את השורה שנוצרה id="data" על ידי ה div ניגש לאלמנט הקיים 
                const element = document.getElementById("data")
                element.appendChild(new_p)
                // div יוצר שני הורדות שורה ומכניס אותם גם כן לאלמנט 
                const new_br = document.createElement("br")
                element.appendChild(new_br)
                const new_br2 = document.createElement("br")
                element.appendChild(new_br2)
                // אם קיימת עוד מכונה ממשיך בלולאה למכונה הבאה
                                }
                        )
                }
         )





