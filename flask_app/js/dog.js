document.addEventListener('DOMContentLoaded', () => {
    const dogSelect = document.querySelector('#dog-select');
    const dogInfo = document.querySelector('#dog-info');
  
    dogSelect.addEventListener('change', () => {
      const selectedDogId = dogSelect.value;
      fetch(`/dog/${selectedDogId}`)
        .then(response => response.json())
        .then(data => {
          dogInfo.innerHTML = `
            <h2>${data.name}</h2>
            <p>Breed: ${data.breed}</p>
            <p>Age: ${data.age}</p>
          `;
        });
    });
  });