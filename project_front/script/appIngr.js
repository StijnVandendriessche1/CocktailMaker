let domData, domHamburger;
let ip = 'http://' + window.location.hostname + ':5000';
//let ip = 'http://192.168.1.53:5000';

const laadCocktails = function(jsonData)
{
    cocktailsHTML = "";
    for(let drank of jsonData)
    {
        cocktailsHTML += 
        `
        <section class="o-row o-row--lg">
			<div class="o-container">
				<div class="o-layout o-layout--align-center o-layout--row-reverse u-green">
					<div class="o-layout__item u-1-of-2-bp3 u-3-of-5-bp4">
						<figure class="c-figure">
							<img src="img/${drank.naam_drank}.jpg" alt="cocktail illustratie">
						</figure>
					</div>
					<div class="o-layout__item u-1-of-2-bp3 u-2-of-5-bp4">
						<div class="u-max-width-sm">
							<h2 class="c-lead c-lead--xl">
								${drank.naam_drank}
							</h2>
						</div>
					</div>
				</div>
			</div>
		</section>
        `;
    }
    domData.innerHTML = cocktailsHTML;
};

const init = function() 
{
    console.log("dom geladen");
    domData = document.querySelector('.js-data');
    handleData(ip + "/api/v1/dranken", laadCocktails);
    domHamburger = document.querySelector('.c-nav__hamburger');
    domHamburger.addEventListener('click', function() 
    {
        console.log("je hebt op de knop gedrukt");
    });
};

document.addEventListener("DOMContentLoaded", init);