let mediaDAta;

const reloadBTN = document.getElementById("refreshLogo");

window.onload = init();
async function init() {
  mediaDAta = await loadDta();
  console.log(mediaDAta);
  generateContent(mediaDAta)
}

async function loadDta() {
  let returnedDAta = await fetch("http://127.0.0.1:5000/media");
  let data = await returnedDAta.json();
  return data;
}

function generateContent(data) {
    const dataCOntainer = document.getElementById("dataCOntainer");
    console.log("probando mierdas",  data)


    for (let i = 0; i < mediaDAta.length; i++) {
        const item = document.createElement("div")
        const img = document.createElement("img")
        const title = document.createElement("h3")
        item.className = "item"
        img.className = "mediaIcon"
        if(data[i].directory !==null){
            // console.log(data[i].directory)
            img.src="./icons/folder.png"
            title.setAttribute('value', data[i].title)
            // console.log(data[i].items_amount)
        }
        else{
            console.log(`algo salio mal ${data[i]}`)
        }
        item.appendChild(img)
        item.appendChild(title)
        dataCOntainer.appendChild(item)

    }
}
