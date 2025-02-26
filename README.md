# KeyLogger
### Tracks an enemy computer. Listens to all its keyboard typing.  
___
## <img src="https://th.bing.com/th/id/R.5cfb779ef6b07d8324a5227b5acff456?rik=C9gC8a%2bwIW1PzQ&riu=http%3a%2f%2fpngimg.com%2fuploads%2fhammer%2fhammer_PNG3890.png&ehk=yvhwJTw1BF8fv%2bjJYlHLI1cB3QsdYPykzGWsqU4%2fnM4%3d&risl=1&pid=ImgRaw&r=0" alt="Hammer" width="20" height="20">  Tools and Technologies:
     


<p>
  <img src="https://cdn.simpleicons.org/css3/1572B6" alt="CSS3" width="30" height="30">
  <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" alt="Python" width="30" height="30">
  <img src="https://cdn.simpleicons.org/javascript/F0DB4F" alt="JavaScript" width="30" height="30">
  <img src="https://cdn.simpleicons.org/html5/E34F26" alt="HTML5" width="30" height="30">
</p>


## Description 
This project is installed on the computer of an enemy. The software will listen to all the typings on the targeted computer.Next, the data will be encrypted and sent to a server computer.
From the server computer the data will be sent directly to your computer through the web decrypted.
___
### In order to use this software, please follow these steps:

1: Clone this project. If you're unfamiliar with the process, watch the following video - https://youtu.be/ILJ4dfOL7zs.  
2: Open your code editor to this project.  
3: Install the "agent" folder on target computer.  
4: On your code editor, in the "agent" folder, run the "main" file. In the "backend" folder, run the "app" file.  
5: You are now set to review all of the target's keyboard pressings by opening the web through the html file of the "frontend" folder.  

## Created by:
Yerucham Mendelson  
Yosef Steinberg  
Benjy Feffer  
Yaakov Sasson  

**Developed, Kodecode course, 2025**


# Countdown Timer

**מאות חוספים על ידי החמאס**

**מחזירים אותם הביתה עכשיו**

<div id="countdown"></div>

<script>
    function countdownTimer() {
        const endDate = new Date("2024-08-01T00:00:00").getTime();
        const now = new Date().getTime();
        const timeLeft = endDate - now;

        const days = Math.floor(timeLeft / (1000 * 60 * 60 * 24));
        const hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);

        document.getElementById("countdown").innerHTML = `${days} days, ${hours} hours, ${minutes} minutes, and ${seconds} seconds`;

        if (timeLeft < 0) {
            clearInterval(timerInterval);
            document.getElementById("countdown").innerHTML = "Time's up!";
        }
    }

    countdownTimer(); // Initial call to display the timer immediately
    const timerInterval = setInterval(countdownTimer, 1000);
</script>
