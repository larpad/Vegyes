const divWork    = document.getElementById("work");
const buttonSend = document.getElementById("send");
buttonSend.addEventListener("click", sendForm);

    function sendForm(){
        lData = CreateJSON_Kozoskoltseg();
        SendDataToServer(lData);
    }
     function CreateJSON_Kozoskoltseg(){
        var files = document.getElementById("pdf").files;
        var file_text = readFile(document.getElementById("pdf").files[0]);

        let reader = new FileReaderSync();
        let result_base64 = reader.readAsDataURL(document.getElementById("pdf").files[0]);


        console.log("out");
        console.log(result_base64);
//        console.log(file_text);

        lKozoskoltseg = {"kozoskoltseg" : { "tipus" : "kozoskoltség"
                                           ,"pdf"   : "PDF"
                                           ,"excel" : "EXCEL"
//                                           ,"pdf_content" : file_text
                                           ,"megjegyzes" : "Megjegyzes"
                                            }};
        console.log("lKozoskoltseg");
        console.log(lKozoskoltseg);
        return JSON.stringify(lKozoskoltseg);
    }
	//--------------------------------------------------------------------------------
    async function readFile(pFile){
        console.log("async");

        let res = await new Promise((resolve) =>{
            let fr = new FileReader();
            fr.onload = (e) => resolve(fr.result);
            fr.readAsDataURL(pFile);
        })

        console.log("in");
//        console.log(res);
        return res;
    }
	//--------------------------------------------------------------------------------
	//--------------------------------------------------------------------------------
/*
        var reader = new FileReader();
        reader.onloadend = function(evt) {
           file_text = evt.target.result;
           console.log("in");
           console.log(file_text);
        }
        reader.readAsDataURL(document.getElementById("pdf").files[0]);
*/
	//--------------------------------------------------------------------------------
    function SendDataToServer(pData){
        let url = "http://127.0.0.1:5000/test";
        Sever_CallServer("POST",url,pData)
    }

    function Sever_CallServer(pType,pURL,pDATA){
        let xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                    Sever_Answer(this.responseText);
            }
        };
        xhr.open(pType,pURL, true);
        xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
        xhr.send(pDATA);
    }

    function Sever_Answer(pData){
        lData = JSON.parse(pData);
        if(lData.hasOwnProperty("kozoskoltseg")) {kiir_kozoskoltseg(lData)}

    }
    function kiir_kozoskoltseg(pData){
        lText = "";
        lText += pData.kozoskoltseg.tipus+"<BR/>"
        lText += pData.kozoskoltseg.pdf+"<BR/>"
        lText += JSON.stringify(pData);
        kiir(lText);
    }

    function kiir(pText){
        divWork.innerHTML = pText;
        console.log(pText);
    }


    //--------------------------------------------------------------------------------
    //--------------------------------------------------------------------------------


/*
		function readFile(file) {
		  return new Promise((resolve, reject) => {
			var reader = new FileReader();
			reader.onload = function() { resolve(reader.result); };
			reader.onerror = reject;
			reader.readAsText(file);
		  });
		}

		async function processFile(file,out_nyaf) {
		  var content = await readFile(file);
		  console.log(content);
		  out_nyaf = content;
		}

		function sendForm(){
			console.log("-- START --");
			console.log("00.01");

			const pdf = document.getElementById("pdf");
//			const excel = document.getElementById("excel");


			console.log(pdf.files[0]);


			const formData = new FormData();

			formData.append('tipus', 'kozoskoltseg');
			formData.append('pdf', pdf.files[0],"file.pdf");
//			formData.append('excel', excel.files[0],"file.xlsx");

			data = JSON.stringify(Object.fromEntries(formData));
			console.log(data);



			var data = { "tipus":"kozoskoltseg",
					      "megjegyzes":"Megjegyzés",
					      "pdf":pdf.files[0].name,
					      "size":pdf.files[0].size,
					      "type":pdf.files[0].type,
					      "value":pdf.files[0].value
					   }
			var TMP;
			 processFile(pdf.files[0],TMP);
			 divWork.innerHTML  = TMP;
/*
			var reader = new FileReader();

			reader.onload = function platy(){
				TMP = reader.result;
				console.log("TMP");
				console.log(TMP);
//				divWork.innerHTML = TMP
			}

//			reader.readAsText(pdf.files[0]);
//			divWork.innerHTML = TMP;
//			reader.readAsDataURL(pdf.files[0]);
//			ileReader.readAsText(file);

//			console.log("01");
//			console.log(reader.result);
//			console.log("02");
//			getText(pdf.files[0]);
//			var new_window = window.open(document.getElementById("pdf").files[0]);
//			new_window.document.write(document.getElementById("pdf").files[0]);
//			window.open(document.getElementById("pdf").files[0]);
//			new_window.document.write(pdf.files[0]);

//			divWork.innerHTML = JSON.stringify(data)
		}
*/

/*
function sayHello() {
//   alert("Hello World");
}
function showEbed() {
   const htmlEbed = '<h1>Ebéd</h1> \
                        <input type="hidden" id="tipus" value="ebed" /> \
                        <p>Kérem a PDF fájlt:</p> \
                        <input type="file" accept=".pdf"  id="pdf"/> \
                        <p>Kérem az Excel fájlt:</p> \
                        <input type="file" accept=".xls"  id="excel"/> \
                        <p>Ha kész indulhat!</p> \
                        <input type="button" value="Feltöltés" onclick="sendForm()">';

   const nodeWork = document.getElementById("work");
   nodeWork.innerHTML = htmlEbed;

}
function showOsztalypenz() {
   alert("Ez ám a lista Lista");

}
function showKozoskoltseg() {
   // alert("Ez ám a lista Lista");
   const htmlEbed = '<h1>Ebéd</h1> \
                        <input type="hidden" id="tipus" value="kozoskoltseg" /> \
                        <p>Kérem a PDF fájlt:</p> \
                        <input type="file" accept=".pdf"  id="pdf"/> \
                        <p>Kérem az Excel fájlt:</p> \
                        <input type="file" accept=".xls"  id="excel"/> \
                        <p>Ha kész indulhat!</p> \
                        <input type="button" value="Feltöltés" onclick="sendForm()">';

   const nodeWork = document.getElementById("work");
   nodeWork.innerHTML = htmlEbed;
}
function showTakaritas() {
   alert("Ez ám a lista Lista");

}

function sendForm() {
   const nodeWork = document.getElementById("work");

   let tipus = document.querySelector("#tipus");
   let pdf = document.querySelector("#pdf");
   let excel = document.querySelector("#excel");

console.log("00");

    const formData = new FormData();
    formData.append('tipus', tipus.value);
    formData.append('pdf', pdf.files[0],"file.pdf");
    formData.append('excel', excel.files[0],"file.xlsx");


console.log("00.01");


const value = Object.fromEntries(formData.entries());
console.log({ value });   }

console.log("01");
console.log(pdf.files[0]);
console.log("02");
    console.log(formData);
console.log("02.01");
    console.log(JSON.stringify(formData));

    console.log(JSON.stringify(formData,entries()));


console.log("03");
    for (let obj of formData) {
        console.log(obj);
    }
console.log("04");
    console.log(formData["tipus"]);

    upload_info = formData;

    console.log(upload_info);

console.log("05");
    var data = JSON.stringify(Object.fromEntries(formData));
   console.log(data);
console.log("06");
console.log(JSON.stringify(data));

    let xhr = new XMLHttpRequest();
    let url = "http://127.0.0.1:5000/create_file";

    // open a connection
    xhr.open("POST", url, true);

    // Set the request header i.e. which type of content you are sending
    xhr.setRequestHeader("Content-Type", "application/json");

    // Create a state change callback
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {

//            nodeWork.innerHTML = this.responseText;
            var new_window = window.open(null, '','_blank');
            new_window.document.write(this.responseText);
        }
    };
    var reader = new FileReader();
    reader.onload = function(e){
        var target = e.target;
        var data = JSON.parse(target.result);
        console.log(data);
    }
    xhr.send(data);
//   alert("Ez ám a lista Lista");
//   nodeWork.innerHTML = "Na ez jól elment";

//    var new_window = window.open(null, '','_blank');
//    new_window.document.write(document.querySelector("#pdf"));
//    var new_window1 = window.open(null, '','_blank');
//    new_window1.document.write(document.querySelector("#pdf").value);
//    var new_window2 = window.open(null, '','_blank');
//    new_window2.document.write(document.querySelector("#pdf").files[0]);

//    var upload_info  = { "tipus": tipus, "pdf" : pdf, "excel" :  excel}

}


function SendDataToServer(pData){
    let xhr = new XMLHttpRequest();
    let url = "http://127.0.0.1:5000/create_file";

    // open a connection
    xhr.open("POST", url, true);

    // Set the request header i.e. which type of content you are sending
//    xhr.setRequestHeader("Content-Type", "application/json");

    // Create a state change callback
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
                SendDataToServer_Response(this.responseText);
        }
    };
    xhr.send(pData);
}
function SendDataToServer_Response(pData){
            var new_window = window.open(null, '','_blank');
            new_window.document.write(this.responseText);
}



function showList() {
   const nodeWork = document.getElementById("work");
//   alert("Ez ám a lista Lista");
   nodeWork.innerHTML = "Ez ám a lista Lista";

}
function file_view(pID){
    alert("Form : " + pID);
 }
*/