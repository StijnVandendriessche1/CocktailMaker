let domData, domHamburger, aanHetWerken;
let ip = 'http://' + window.location.hostname + ':5000';
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
				<div class="o-layout o-layout--align-center o-layout--row u-green">
					<div class="o-layout__item u-1-of-3-bp3 u-1-of-5-bp4">
						<figure class="c-figure">
							<img src="img/${cocktail.naam_cocktail}.jpg" alt="cocktail illustratie">
						</figure>
					</div>
					<div class="o-layout__item u-2-of-2-bp3 u-4-of-5-bp4">
						<div class="u-max-width-sm">
							<h2 class="c-lead c-lead--xl">
								${cocktail.naam_cocktail}
							</h2>
							<p>
								<a class="c-link-cta" href="#!" id="${cocktail.code_cocktail}">
									Maak cocktail
								</a>
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
    handleData(ip + "/api/v1/cocktails", laadCocktails);
    //domHamburger = document.querySelector('.c-nav__hamburger');
    //domHamburger.addEventListener('click', function() 
    //{
        //console.log("je hebt op de knop gedrukt");
    //});
};

document.addEventListener("DOMContentLoaded", init);