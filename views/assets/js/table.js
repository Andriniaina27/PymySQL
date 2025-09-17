// On récupère le wrapper existant
const wrapper = document.getElementById("wrapper");

// ====== Sidebar ======
const sidebar = document.createElement("div");
sidebar.className = "sidebar";
sidebar.id = "sidebar";

const nav = document.createElement("nav");

// Heading
const heading = document.createElement("div");
heading.className = "heading";
const h3Heading = document.createElement("h3");
h3Heading.textContent = "Admin";
heading.appendChild(h3Heading);
nav.appendChild(heading);

// Nav links
const navlink = document.createElement("div");
navlink.className = "navlink";

const links = [
    { href: "", icon: "fa-user", text: "Dashboard" },
    { href: "", icon: "fa-user", text: "Dashboard" },
    { href: "create.html", icon: "fa-user", text: "Create" },
    { href: "", icon: "fa-user", text: "Dashboard" },
];

links.forEach(l => {
    const a = document.createElement("a");
    a.href = l.href;
    a.className = "nav-item";

    const i = document.createElement("i");
    i.className = `fa ${l.icon}`;
    a.appendChild(i);

    const text = document.createTextNode(" " + l.text);
    a.appendChild(text);

    navlink.appendChild(a);
});

nav.appendChild(navlink);
sidebar.appendChild(nav);

// ====== Content Table ======
const content = document.createElement("div");
content.className = "content-table";

// Head
const headDiv = document.createElement("div");
headDiv.className = "head";

const searchInput = document.createElement("input");
searchInput.type = "text";
searchInput.id = "search";
searchInput.placeholder = "Recherche....";

const iconDiv = document.createElement("div");
iconDiv.className = "icon";

const menuIcon = document.createElement("i");
menuIcon.className = "fa fa-bars";
menuIcon.id = "menu-btn";

iconDiv.appendChild(menuIcon);
headDiv.appendChild(searchInput);
headDiv.appendChild(iconDiv);
content.appendChild(headDiv);

// Titre section
const titreDiv = document.createElement("div");
titreDiv.className = "titre";

const h3Titre = document.createElement("h3");
h3Titre.textContent = "Tableau";

const addBtn = document.createElement("a");
addBtn.href = "/touristeInsert";
addBtn.className = "btn";

const plusIcon = document.createElement("i");
plusIcon.className = "fa fa-plus-circle";

addBtn.appendChild(plusIcon);
titreDiv.appendChild(h3Titre);
titreDiv.appendChild(addBtn);
content.appendChild(titreDiv);

// Container table
const containerDiv = document.createElement("div");
containerDiv.className = "container";

const tableDiv = document.createElement("div");
tableDiv.className = "table";

const table = document.createElement("table");

// Table head
const thead = document.createElement("thead");
const trHead = document.createElement("tr");
["Nom", "Prenom", "Age", "Groupe", "Action"].forEach(text => {
    const th = document.createElement("th");
    th.textContent = text;
    trHead.appendChild(th);
});
thead.appendChild(trHead);
table.appendChild(thead);

// Table body

// Données exemple
// const table_touristes = [
//     { nom: "Harena", prenom: "Jorginho", age: 14, groupe: "6" },
//     { nom: "Luca", prenom: "Andriniaina", age: 15, groupe: "3" }
// ];

// table_touristes.forEach(t => {
    //     const tr = document.createElement("tr");

//     ["nom", "prenom", "age", "groupe"].forEach(k => {
//         const td = document.createElement("td");
//         td.textContent = t[k];
//         tr.appendChild(td);
//     });

//     const actionTd = document.createElement("td");
//     const btn = document.createElement("button");
//     btn.textContent = "Supprimer";
//     actionTd.appendChild(btn);
//     tr.appendChild(actionTd);

//     tbody.appendChild(tr);
// });

// const tbody = document.getElementById("tbody");
// table.appendChild(tbody);
tableDiv.appendChild(table);
containerDiv.appendChild(tableDiv);
content.appendChild(containerDiv);

// ====== Ajouter Sidebar et Content dans le wrapper existant ======
wrapper.appendChild(sidebar);
wrapper.appendChild(content);


// const btn = document.getElementById("menu-btn");
// const sidebar = document.getElementById("sidebar");

document.getElementById("menu-btn").addEventListener("click", function () {
      // bascule la classe active
    document.getElementById("sidebar").classList.toggle("active");
});

search.addEventListener("input", function () {
    let input = search.value.toLowerCase();
    let rows = document.querySelectorAll("table tbody tr");

    rows.forEach(function (row) {
    //   let nom = row.cells[0].textContent.toLowerCase();
      let cells = Array.from(row.cells)
    //   let resultat = nom.includes(input);
      let match = cells.some(cell => cell.textContent.toLowerCase().includes(input))
      
      row.style.display = match ? "" : "none";
    });
});
