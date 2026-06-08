const API_BASE = "http://localhost:3001/api";
let currentPokemon = null; // Store current searched Pokemon

// Common Pokemon names for autocomplete
const pokemonNames = [
  "bulbasaur",
  "ivysaur",
  "venusaur",
  "charmander",
  "charmeleon",
  "charizard",
  "squirtle",
  "wartortle",
  "blastoise",
  "caterpie",
  "metapod",
  "butterfree",
  "weedle",
  "kakuna",
  "beedrill",
  "pidgey",
  "pidgeotto",
  "pidgeot",
  "rattata",
  "raticate",
  "spearow",
  "fearow",
  "ekans",
  "arbok",
  "pikachu",
  "raichu",
  "sandshrew",
  "sandslash",
  "nidoran-f",
  "nidorina",
  "nidoqueen",
  "nidoran-m",
  "nidorino",
  "nidoking",
  "clefairy",
  "clefable",
  "vulpix",
  "ninetales",
  "jigglypuff",
  "wigglytuff",
  "zubat",
  "golbat",
  "oddish",
  "gloom",
  "vileplume",
  "paras",
  "parasect",
  "venonat",
  "venomoth",
  "diglett",
  "dugtrio",
  "meowth",
  "persian",
  "psyduck",
  "golduck",
  "mankey",
  "primeape",
  "growlithe",
  "arcanine",
  "poliwag",
  "poliwhirl",
  "poliwrath",
  "abra",
  "kadabra",
  "alakazam",
  "machop",
  "machoke",
  "machamp",
  "bellsprout",
  "weepinbell",
  "victreebel",
  "tentacool",
  "tentacruel",
  "geodude",
  "graveler",
  "golem",
  "ponyta",
  "rapidash",
  "slowpoke",
  "slowbro",
  "magnemite",
  "magneton",
  "farfetchd",
  "doduo",
  "dodrio",
  "seel",
  "dewgong",
  "grimer",
  "muk",
  "shellder",
  "cloyster",
  "gastly",
  "haunter",
  "gengar",
  "onix",
  "drowzee",
  "hypno",
  "krabby",
  "kingler",
  "voltorb",
  "electrode",
  "exeggcute",
  "exeggutor",
  "cubone",
  "marowak",
  "hitmonlee",
  "hitmonchan",
  "lickitung",
  "koffing",
  "weezing",
  "rhyhorn",
  "rhydon",
  "chansey",
  "tangela",
  "kangaskhan",
  "horsea",
  "seadra",
  "goldeen",
  "seaking",
  "staryu",
  "starmie",
  "mr-mime",
  "scyther",
  "jynx",
  "electabuzz",
  "magmar",
  "pinsir",
  "tauros",
  "magikarp",
  "gyarados",
  "lapras",
  "ditto",
  "eevee",
  "vaporeon",
  "jolteon",
  "flareon",
  "porygon",
  "omanyte",
  "omastar",
  "kabuto",
  "kabutops",
  "aerodactyl",
  "snorlax",
  "articuno",
  "zapdos",
  "moltres",
  "dratini",
  "dragonair",
  "dragonite",
  "mewtwo",
  "mew",
];

let selectedSuggestionIndex = -1; // Track selected suggestion

// Load Pokemon collection on page load
document.addEventListener("DOMContentLoaded", () => {
  loadPokemonCollection();
  setupSearchAutocomplete();
});

function setupSearchAutocomplete() {
  const input = document.getElementById("searchInput");
  const dropdown = document.getElementById("autocompleteDropdown");

  input.addEventListener("input", handleInput);
  input.addEventListener("keydown", handleKeydown);
  input.addEventListener("blur", () => {
    // Delay hiding to allow clicks on dropdown items
    setTimeout(() => hideDropdown(), 150);
  });
  input.addEventListener("focus", () => {
    if (input.value.trim()) {
      showSuggestions(input.value.trim());
    }
  });

  function handleInput(e) {
    const query = e.target.value.trim();
    selectedSuggestionIndex = -1;

    if (query) {
      showSuggestions(query);
    } else {
      hideDropdown();
    }
  }

  function handleKeydown(e) {
    const items = dropdown.querySelectorAll(".autocomplete-item");

    switch (e.key) {
      case "ArrowDown":
        e.preventDefault();
        selectedSuggestionIndex = Math.min(
          selectedSuggestionIndex + 1,
          items.length - 1,
        );
        updateSelection();
        break;
      case "ArrowUp":
        e.preventDefault();
        selectedSuggestionIndex = Math.max(
          selectedSuggestionIndex - 1,
          -1,
        );
        updateSelection();
        break;
      case "Enter":
        e.preventDefault();
        if (
          selectedSuggestionIndex >= 0 &&
          items[selectedSuggestionIndex]
        ) {
          selectSuggestion(items[selectedSuggestionIndex].textContent);
        } else {
          searchPokemon();
        }
        break;
      case "Escape":
        hideDropdown();
        input.blur();
        break;
    }
  }

  function updateSelection() {
    const items = dropdown.querySelectorAll(".autocomplete-item");
    items.forEach((item, index) => {
      item.classList.toggle(
        "selected",
        index === selectedSuggestionIndex,
      );
    });

    // Scroll selected item into view
    if (selectedSuggestionIndex >= 0 && items[selectedSuggestionIndex]) {
      items[selectedSuggestionIndex].scrollIntoView({
        block: "nearest",
        behavior: "smooth",
      });
    }
  }

  function showSuggestions(query) {
    const filtered = pokemonNames
      .filter((name) =>
        name.toLowerCase().startsWith(query.toLowerCase()),
      )
      .slice(0, 8); // Limit to 8 suggestions

    if (filtered.length === 0) {
      hideDropdown();
      return;
    }

    dropdown.innerHTML = filtered
      .map((name) => `<div class="autocomplete-item">${name}</div>`)
      .join("");

    // Add click handlers
    dropdown
      .querySelectorAll(".autocomplete-item")
      .forEach((item, index) => {
        item.addEventListener("click", () =>
          selectSuggestion(item.textContent),
        );
        item.addEventListener("mouseenter", () => {
          selectedSuggestionIndex = index;
          updateSelection();
        });
      });

    dropdown.classList.add("show");
  }

  function hideDropdown() {
    dropdown.classList.remove("show");
    selectedSuggestionIndex = -1;
  }

  function selectSuggestion(name) {
    input.value = name;
    hideDropdown();
    searchPokemon();
  }
}

async function loadPokemonCollection() {
  try {
    const response = await fetch(`${API_BASE}/pokemon`);
    const pokemon = await response.json();

    const container = document.getElementById("pokemonContainer");

    if (pokemon.length === 0) {
      container.innerHTML = `
        <div style="grid-column: 1/-1; text-align: center;">
          <div class="empty-state">
            <p>Your collection is empty. Search for a Pokemon to get started!</p>
          </div>
        </div>
      `;
      return;
    }

    container.innerHTML = pokemon
      .map(
        (p) => `
      <div class="pokemon-card">
        <div class="card-image">
          <img src="${p.image_url}" alt="${p.name}" onerror="this.style.display='none'">
        </div>
        <div class="card-content">
          <div class="card-name">${p.name}</div>
          <div class="card-types">
            ${p.types.map((t) => `<span class="card-type">${t}</span>`).join("")}
          </div>
          <div class="card-stats">
            <div>Height: ${(p.height / 10).toFixed(1)}m</div>
            <div>Weight: ${(p.weight / 10).toFixed(1)}kg</div>
          </div>
          <button class="delete-button" onclick="deletePokemon(${p.id}, '${p.name}')">
            Delete from Collection
          </button>
        </div>
      </div>
    `,
      )
      .join("");
  } catch (error) {
    console.error("Error loading collection:", error);
    document.getElementById("pokemonContainer").innerHTML = `
      <div style="grid-column: 1/-1;">
        <div class="error">Failed to load collection. Make sure the backend is running on port 3001.</div>
      </div>
    `;
  }
}

async function searchPokemon() {
  // Hide autocomplete dropdown
  const dropdown = document.getElementById("autocompleteDropdown");
  dropdown.classList.remove("show");

  const input = document.getElementById("searchInput");
  const query = input.value.trim();

  if (!query) {
    alert("Please enter a Pokemon name");
    return;
  }

  const resultDiv = document.getElementById("searchResult");
  resultDiv.innerHTML = '<div class="loading">Searching...</div>';
  resultDiv.classList.add("show");

  try {
    const response = await fetch(`${API_BASE}/search/${query}`);

    if (!response.ok) {
      resultDiv.innerHTML = `
        <div class="error">Pokemon not found. Try another name!</div>
      `;
      return;
    }

    const pokemon = await response.json();
    currentPokemon = pokemon; // Store for add function

    resultDiv.innerHTML = `
      <div class="pokemon-preview">
        <div class="pokemon-image">
          <img src="${pokemon.image_url}" alt="${pokemon.name}" onerror="this.style.display='none'">
        </div>
        <div class="pokemon-details">
          <h3>${pokemon.name}</h3>
          <div class="types">
            ${pokemon.types.map((t) => `<span class="type">${t}</span>`).join("")}
          </div>
          <div class="pokemon-info">
            <div class="info-item"><strong>Height:</strong> ${(pokemon.height / 10).toFixed(1)}m</div>
            <div class="info-item"><strong>Weight:</strong> ${(pokemon.weight / 10).toFixed(1)}kg</div>
            <div class="info-item"><strong>Base Experience:</strong> ${pokemon.base_experience}</div>
            <div class="info-item"><strong>HP:</strong> ${pokemon.stats.find((s) => s.name === "hp")?.value || "N/A"}</div>
          </div>
          <div class="stats">
            <h4>Base Stats</h4>
            ${pokemon.stats
              .map(
                (stat) => `
              <div class="stat-item">
                <span style="text-transform: capitalize; min-width: 70px;">${stat.name}:</span>
                <div class="stat-bar">
                  <div class="stat-fill" style="width: ${(stat.value / 255) * 100}%"></div>
                </div>
                <span style="min-width: 30px; text-align: right;">${stat.value}</span>
              </div>
            `,
              )
              .join("")}
          </div>
          <button class="add-button" onclick="addCurrentPokemon()">
            Add to Collection
          </button>
          <div id="addMessage"></div>
        </div>
      </div>
    `;
  } catch (error) {
    console.error("Search error:", error);
    resultDiv.innerHTML = `
      <div class="error">Error searching Pokemon. Make sure the backend is running.</div>
    `;
  }
}

async function addCurrentPokemon() {
  if (!currentPokemon) {
    alert("No Pokemon selected");
    return;
  }

  try {
    const response = await fetch(`${API_BASE}/pokemon`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        pokemon_id: currentPokemon.pokemon_id,
        name: currentPokemon.name,
        height: currentPokemon.height,
        weight: currentPokemon.weight,
        base_experience: currentPokemon.base_experience,
        image_url: currentPokemon.image_url,
        types: currentPokemon.types,
        stats: currentPokemon.stats,
      }),
    });

    const messageDiv = document.getElementById("addMessage");

    if (!response.ok) {
      const error = await response.json();
      messageDiv.innerHTML = `<div class="error">${error.error}</div>`;
      return;
    }

    messageDiv.innerHTML = `<div class="success">✓ ${currentPokemon.name} added to your collection!</div>`;
    setTimeout(() => {
      loadPokemonCollection();
      document.getElementById("searchResult").classList.remove("show");
      document.getElementById("searchInput").value = "";
      messageDiv.innerHTML = "";
    }, 1000);
  } catch (error) {
    console.error("Add error:", error);
    document.getElementById("addMessage").innerHTML = `
      <div class="error">Error adding Pokemon</div>
    `;
  }
}

async function deletePokemon(id, name) {
  if (
    !confirm(
      `Are you sure you want to remove ${name} from your collection?`,
    )
  ) {
    return;
  }

  try {
    const response = await fetch(`${API_BASE}/pokemon/${id}`, {
      method: "DELETE",
    });

    if (!response.ok) {
      alert("Error deleting Pokemon");
      return;
    }

    loadPokemonCollection();
  } catch (error) {
    console.error("Delete error:", error);
    alert("Error deleting Pokemon");
  }
}
