function confirmDelete_p (event_opl) {
	if((event_opl.target.tagName.toLowerCase()=='a')&&(event_opl.target.className=="clDelete")) 
	{
		 
		antwort = confirm("Wollen Sie den Eintrag wirklich löschen?");
        if(antwort != true)
		{
            event_opl.preventDefault();
			alert("Löschen abgebrochen.");
        }else{
            alert("Löschen erfolgreich.");
        }
	}
		
}


window.onload = function () {
	let body_o = document.getElementsByTagName('body')[0];
	body_o.addEventListener('click',confirmDelete_p,false);
}
