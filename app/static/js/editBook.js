const body = document.querySelector("body"),
      sidebar = body.querySelector(".sidebar"),
      toggle = body.querySelector(".toggle"),
	  modeSwitch = body.querySelector(".toggle-switch"),
	  modeText = body.querySelector(".mode-text");

const optionBar = document.querySelector("rate-area")
	   	
const img = document.getElementById('logo');  
const img2 = document.getElementById('logo2');  
const togg = document.getElementById('arrow');
const moon = document.getElementById('moon');
const sun = document.getElementById('sun');
const homeMode = document.getElementById('homeMode');

const img_line2 = document.getElementById('line2'); 

const home = document.querySelector("home"),
      row =  document.querySelector("row"),
      card = document.querySelector("card"),
      cardImg = document.querySelector("card-img-top");

let mode = false;
let closeMode = false;	  
togg.style.rotate = '180deg';
togg.style.top = "0%";

	   toggle.addEventListener("click", () =>{
	   sidebar.classList.toggle("close");
		 
		 if(!closeMode){ 
			togg.style.top = "36%";
			togg.style.rotate = '0deg';
            img2.style.opacity = '1';
			closeMode = true;

		}else{
			togg.style.top = "0%";
			togg.style.rotate = '180deg';
            img2.style.opacity = '1';		
			closeMode = false;
			}  
	  });
	  
	  modeSwitch.addEventListener("click", () =>{
		  body.classList.toggle("dark");
		  
		if(!mode){
			sun.style.opacity = '1';
			moon.style.opacity = '0';
			img.src = "../static/logo1_b.png";
			img.style.trasition = 'all 0.2s ease';
			modeText.innerText = "Light Mode"
			modeText.setAttribute.value = "1"	
            img2.src = "../static/logo2.png";
			img_line2.src = "../static/line_dark_mode.png";

			mode = true;
			document.getElementById('modeText').value = "1";
		}else{
			sun.style.opacity = '0';
			moon.style.opacity = '1';
			img.src = "../static/logo1_d.png";  
			img.style.trasition = 'all 0.2s ease';
			modeText.innerText = "Dark Mode"
			modeText.setAttribute.value = "0"
            img2.src = "../static/logo2_d.png";
			img_line2.src = "../static/line.png"				  
			mode = false;
			document.getElementById('modeText').value = "0";
		}
				
	  });