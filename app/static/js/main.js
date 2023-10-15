const body = document.querySelector("body"),
      sidebar = body.querySelector(".sidebar"),
      toggle = body.querySelector(".toggle"),
	  search = body.querySelector(".searchBtn"),
	  icon2 = body.querySelector(".icon2"),
	  modeSwitch = body.querySelector(".toggle-switch"),
	  modeText = body.querySelector(".mode-text");


const optionBar = document.querySelector("rate-area")
	   	

const search_box_imput = document.getElementById('searchBox'); 
const img = document.getElementById('logo');  
const img2 = document.getElementById('logo2');  
const togg = document.getElementById('arrow');
const moon = document.getElementById('moon');
const sun = document.getElementById('sun');
const homeMode = document.getElementById('homeMode');

const iconBtn = document.getElementById('iconBtni');

const sortZA = document.getElementById('ZA');
const searchBox = document.getElementById('sBox');

const home = document.querySelector("home"),
      row =  document.querySelector("row"),
      card = document.querySelector("card"),
      cardImg = document.querySelector("card-img-top");

	  sBox = body.querySelector(".form-control");  

let mode = false;
let closeMode = false;	  
togg.style.rotate = '180deg';
togg.style.top = "0%";
icon2.style.zIndex= '10';
search.style.opacity = '1';
search.style.zIndex = '0';	
sBox.style.width = '203px';
search_box_imput.style.opacity = "1";


	   toggle.addEventListener("click", () =>{
	   sidebar.classList.toggle("close");
		 
		 if(!closeMode){ 
			togg.style.top = "36%";
			togg.style.rotate = '0deg';
            img2.style.opacity = '1';
			homeMode.style.width = '80%';
			search.style.opacity = '0';
			search.style.zIndex = '-9';
			sBox.style.width = '50px';
			search_box_imput.style.opacity = "0";
			icon2.style.color = "#000";
			closeMode = true;

		}else{
			togg.style.top = "0%";
			togg.style.rotate = '180deg';
            img2.style.opacity = '1';
			homeMode.style.width = '96%';			
			search.style.opacity = '1';
			search.style.zIndex = '9';
			sBox.style.width = '203px';
			search_box_imput.style.opacity = "1";
			icon2.style.color = "#fff";
			closeMode = false;
			}  
	  });
	  
	      searchBox.addEventListener("click", () =>{
		  sidebar.classList.remove("close");
		   
		 if(closeMode){ 
		    togg.style.rotate = '180deg';
			togg.style.top = "0%";
            img2.style.opacity = '1';
			search.style.opacity = '1';
            search.style.zIndex = '9';
			sBox.style.width = '203px';
			search_box_imput.style.opacity = "1";
			icon2.style.color = "#fff";
			closeMode = false;
		}
			});
		
			icon2.addEventListener("click", () =>{
				sidebar.classList.remove("close");
				 
			   if(closeMode){ 
				  togg.style.rotate = '180deg';
				  togg.style.top = "0%";
				  img2.style.opacity = '1';
				  search.style.opacity = '1';
				  search.style.zIndex = '9';
				  sBox.style.width = '203px';
				  search_box_imput.style.opacity = "1";
				  icon2.style.color = "#fff";
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
			line.src = "../static/line_dark_mode.png";
			line2.src = "../static/line_dark_mode.png";
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
			line.src = "../static/line.png";
			line2.src = "../static/line.png"				  
			mode = false;
			document.getElementById('modeText').value = "0";
		}
				
	  });

	  
	


