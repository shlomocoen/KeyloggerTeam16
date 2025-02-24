
fetch("http://127.0.0.1:5000/api/get_target_machines_list").then(
    response => response.json()

    ).then(
        data => {
            console.log(data)
            const list = data.machines
            
            list.forEach(item => {
                const new_br = document.createElement("p")
                console.log(item)
                const new_element = document.createElement("a")
                const element = document.getElementById("data")
                new_element.href = `8200p3.html?computer=${item}`
                new_element.setAttribute('class', 'button1')
                new_element.textContent = item
                console.log(new_element)
                new_br.appendChild(new_element)
                console.log("!!!!!!!!!")
                element.appendChild(new_br)
                const new_br2 = document.createElement("br")
                element.appendChild(new_br2)
                const new_br3 = document.createElement("br")
                element.appendChild(new_br3)

                                }
                        )
                }
         )





