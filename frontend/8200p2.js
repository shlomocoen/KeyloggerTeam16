
fetch("http://127.0.0.1:5000/api/get_target_machines_list").then(
    response => response.json()

    ).then(
        data => {
            console.log(data)
            const list = data.machines
            
            list.forEach(item => {
                console.log(item)
                const new_element = document.createElement("a")
                const element = document.getElementById("data")
                new_element.href = '8200p3.html'
                new_element.setAttribute('class', 'button1')
                new_element.textContent = item
                console.log(new_element)
                element.appendChild(new_element)
                console.log("!!!!!!!!!")
                                }
                        )
                }
         )





