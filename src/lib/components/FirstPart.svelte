<script lang="js">
    import Hidden from '$lib/components/Hidden.svelte';

    let show;
    let shown;

    let show2;
    let shown2;

    let show3;
    let shown3;
</script>


<div id="firstPart">
    <div class="
        flex justify-center space-x-3 py-5
        text-5xl
        font-semibold">
        <h1>
            I - Présentation de l'expérience
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
                    1 - Le Protocole
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
                    flex justify-evenly py-3
                    text-2xl">
                    <div class="w-2/7">
                        <img class="rounded-t-xl" src="protocol/picture2.png" alt="">
                        <div class="
                            px-3 py-3 
                            rounded-b-xl 
                            bg-purple-900">
                            <p class="h-32
                                text-justify">
                                Solution d'Eau, d'Ethanol et de Chlorure de Cuivre dans un creuset.
                            </p>
                        </div>
                    </div>
                    <div class="w-2/7">
                        <img class="
                            rounded-t-xl" 
                            src="protocol/picture3.png" 
                            alt="">
                        <div class="
                            px-3 py-3 
                            rounded-b-xl 
                            bg-purple-900">
                            <p class="h-32
                                text-justify">
                                Matériel (de gauche a droite) : Ethanol, Chalumeau, Chlorure de Cuivre, 
                                Nitrate de Baryum, Chlorure de Sodium, Gaz pour le Chalumeau.
                            </p>
                        </div>
                    </div>
                    <div class="w-2/7">
                        <img class="
                            rounded-t-xl" 
                            src="protocol/picture4.png" 
                            alt="">
                        <div class="
                            px-3 py-3 
                            rounded-b-xl 
                            bg-purple-900">
                            <p class="h-32
                                text-justify">
                                Creuset d'Eau distillée, d'Ethanol et de Chlorure de Cuivre, 
                                Eau distillée dans la coupelle de gauche et Ethanol dans celle de droite. 
                                Le Bécher sert de poubelle.
                            </p>
                        </div>
                    </div>
                </div>
            </Hidden>
            <div class="
                flex justify-center self-center space-x-2
                text-4xl
                font-normal">
                <h2>
                    2 - Les Résultats
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
                    flex justify-center py-3">
                    <div class="w-5/7 
                        text-2xl">
                        <img class="
                            rounded-t-xl" 
                            src="menu-pics/barium_nitrate.png" 
                            alt="">
                        <h1 class="h-auto
                            flex justify-center px-2 py-2
                            rounded-b-xl
                            bg-purple-900">
                            Spectre lumineux d'une flamme de Nitrate de Barium
                        </h1>
                    </div>
                </div>
                <div class="
                    flex justify-center py-3">
                    <div class="w-5/7 
                        text-2xl">
                        <img class="
                            rounded-t-xl" 
                            src="menu-pics/sodium_chloride.png" 
                            alt="">
                        <h1 class="h-auto
                            flex justify-center px-2 py-2
                            rounded-b-xl
                            bg-purple-900">
                            Spectre lumineux d'une flamme de Chlorure de Sodium
                        </h1>
                    </div>
                </div>
                <div class="
                    flex justify-center py-3">
                    <div class="w-5/7 
                        text-2xl">
                        <img class="
                            rounded-t-xl" 
                            src="menu-pics/copper_chloride.png" 
                            alt="">
                        <h1 class="h-auto
                            flex justify-center px-2 py-2
                            rounded-b-xl
                            bg-purple-900">
                            Spectre lumineux d'une flamme de Chlorure de Cuivre
                        </h1>
                    </div>
                </div>
            </Hidden>
        </div>
    </Hidden>
</div>