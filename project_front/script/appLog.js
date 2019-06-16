let domData, domHamburger, aanHetWerken;
let ip = 'http://'+ window.location.hostname +':5000';
//let ip = 'http://192.168.1.53:5000';

const cocktailResponse = function(jsonData) 
{
    aanHetWerken = false;
    window.alert(jsonData);
};

const listenToMaakCocktail = function() 
{
    for(let cocktail of domData.children)
    {
        cocktail.firstElementChild.firstElementChild.lastElementChild.firstElementChild.lastElementChild.firstElementChild.addEventListener('click', function() 
        {
            if(!aanHetWerken)
            {
                id = this.id;
                aanHetWerken = true;
                handleData(ip + `/api/v1/cocktail/${id}`, cocktailResponse);
            }
            else
            {
                window.alert("Er wordt momenteel al een cocktail gemaakt.");
            }
        });
    }
};

const laadCocktails = function(jsonData)
{
    cocktailsHTML = "";
    for(let cocktail of jsonData)
    {
        cocktailsHTML += 
        `
        <section class="o-row o-row--lg">
			<div class="o-container">
				<div class="o-layout o-layout--align-center o-layout--row-reverse u-green">
					<div class="o-layout__item">
						<div class="u-max-width-sm">
							<h2 class="c-lead c-lead--xl">
								${cocktail.naam_cocktail}
							</h2>
							<p>
                                ${cocktail.datum}
							</p>
						</div>
					</div>
				</div>
			</div>
		</section>
        `;
    }
    domData.innerHTML = cocktailsHTML;
    listenToMaakCocktail();
};

const init = function() 
{
    console.log("dom geladen");
    domData = document.querySelector('.js-data');
    handleData(ip + "/api/v1/logboek", laadCocktails);
    //domHamburger = document.querySelector('.c-nav__hamburger');
    //domHamburger.addEventListener('click', function() 
    //{
        //console.log("je hebt op de knop gedrukt");
    //});
};

document.addEventListener("DOMContentLoaded", init);