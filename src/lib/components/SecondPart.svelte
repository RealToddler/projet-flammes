<script lang="js">
    import Hidden from '$lib/components/Hidden.svelte';

    let show;
    let shown;

    let show2;
    let shown2;

    let show3;
    let shown3;
</script>


<div id="secondPart">
    <div class="
        flex justify-center space-x-3 py-5
        text-5xl
        font-semibold">
        <h1>
            II - Explications
        </h1>
        <button on:click = {show}
            style="outline:none;">
            {#if shown}
                <svg xmlns="http://www.w3.org/2000/svg" 
                    class="h-8 w-8 
                        self-center" 
                    fill="none" 
                    viewBox="0 0 24 24" 
                    stroke="currentColor" 
                    stroke-width="2">
                    <path stroke-linecap="round" 
                        stroke-linejoin="round"
                        d="M5 15l7-7 7 7" />
                </svg>
            {:else}
                <svg xmlns="http://www.w3.org/2000/svg" 
                    class="h-8 w-8 
                        self-center" 
                    fill="none" 
                    viewBox="0 0 24 24" 
                    stroke="currentColor" 
                    stroke-width="2">
                    <path stroke-linecap="round" 
                        stroke-linejoin="round" 
                        d="M19 9l-7 7-7-7" />
                </svg>
            {/if}
        </button>
    </div>
    <Hidden bind:shown bind:show>
        <div class="
            space-y-5">                
            <div class="
                flex justify-center self-center space-x-2
                text-4xl
                font-normal">
                <h2>
                    1 - Les Combustibles
                </h2>
                <button on:click = {show2}
                    style="outline:none;">
                    {#if shown2}
                        <svg xmlns="http://www.w3.org/2000/svg" 
                            class="h-6 w-6 
                                self-center" 
                            fill="none" 
                            viewBox="0 0 24 24" 
                            stroke="currentColor" 
                            stroke-width="1.5">
                            <path stroke-linecap="round" 
                                stroke-linejoin="round"
                                d="M5 15l7-7 7 7" />
                        </svg>
                    {:else}
                        <svg xmlns="http://www.w3.org/2000/svg" 
                            class="h-7 w-7 
                                self-center" 
                            fill="none" 
                            viewBox="0 0 24 24" 
                            stroke="currentColor" 
                            stroke-width="1.5">
                            <path stroke-linecap="round" 
                                stroke-linejoin="round" 
                                d="M19 9l-7 7-7-7" />
                        </svg>
                    {/if}
                </button>
            </div>
            <Hidden bind:shown2 bind:show2>
                <div class="
                    flex justify-evenly py-3">
                    <div class="w-2/7">
                        <img class="rounded-t-xl" 
                            src="flames/picture7.png" 
                            alt="">
                        <div class="h-15
                            flex justify-center self-center
                            rounded-b-xl
                            text-2xl 
                            bg-purple-900">
                            <h1 class="
                                self-center">
                                Flamme de Nitrate de Barium
                            </h1>
                        </div>
                    </div>
                    <div class="w-2/7">
                        <img class="
                            rounded-t-xl"
                            src="flames/picture6.png" 
                            alt="">
                        <div class="h-15
                            flex justify-center self-center
                            rounded-b-xl
                            text-2xl 
                            bg-purple-900">
                            <h1 class="
                                self-center">
                                Flamme de Chlorure de Cuivre
                            </h1>
                        </div>
                    </div>
                    <div class="w-2/7">
                        <img class="
                            rounded-t-xl"
                            src="flames/picture5.png" 
                            alt="">
                        <div class="h-15
                            flex justify-center self-center
                            rounded-b-xl
                            text-2xl 
                            bg-purple-900">
                            <h1 class="
                                self-center">
                                Flamme de Chlorure de Sodium
                            </h1>
                        </div>
                    </div>
                </div>
            </Hidden>
            <div class="
                flex justify-center self-center space-x-2
                text-4xl
                font-normal">
                <h2>
                    2 - La Chaleur de la Flamme
                </h2>
                <button on:click = {show3}
                    style="outline:none;">
                    {#if shown3}
                        <svg xmlns="http://www.w3.org/2000/svg" 
                            class="h-7 w-7 
                                self-center" 
                            fill="none" 
                            viewBox="0 0 24 24" 
                            stroke="currentColor" 
                            stroke-width="1.5">
                            <path stroke-linecap="round" 
                                stroke-linejoin="round"
                                d="M5 15l7-7 7 7" />
                        </svg>
                    {:else}
                        <svg xmlns="http://www.w3.org/2000/svg" 
                            class="h-7 w-7 
                                self-center" 
                            fill="none" 
                            viewBox="0 0 24 24" 
                            stroke="currentColor" 
                            stroke-width="1.5">
                            <path stroke-linecap="round" 
                                stroke-linejoin="round" 
                                d="M19 9l-7 7-7-7" />
                        </svg>
                    {/if}
                </button>
            </div>
            <Hidden bind:shown3 bind:show3>
                <div class="
                    flex justify-center py-5">
                    <div class="space-y-5">
                        <img class="w-6/7
                            rounded-xl" 
                            src="menu-pics/wien_law.png" 
                            alt="">
                        <img class="w-6/7
                            rounded-xl" 
                            src="menu-pics/warm_spectrum.png" 
                            alt="">
                    </div>
                    <div class="self-center">
                        <img class="
                            rounded-xl" 
                            src="menu-pics/explained_flame.png" 
                            alt="">
                    </div>
                </div>
                <p class="w-5/7
                    flex mx-auto py-5 px-5
                    rounded-xl border-3
                    text-2xl text-justify
                    font-normal">
                    La température de la flamme influe sur sa couleur. Ainsi, plus la couleur de la flamme sera chaude, 
                    plus la température sera basse inversement, plus la couleur de la flamme sera froide plus sa température sera élevée. 
                    Ce phénomène est dû à l’excitation des électrons et des composés métalliques présents dans les flammes. 
                    Ces derniers restituent l’énergie sous la forme d’une émission lumineuse spécifique. 
                </p>
            </Hidden>   
        </div>
    </Hidden>
</div>