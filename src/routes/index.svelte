<script lang="js">
    import * as animateScroll from "svelte-scrollto";
    import ExpExplains from '$lib/components/ExpExplains.svelte'

    let shown1, show1
    let shown11, show11
    let shown12, show12

    let shown2, show2
    let shown21, show21
    let shown22, show22
</script>



<!--Problématique-->
<div id="pbq"
    style="background-image: url(backgrounds/index_pbq_bg.png); background-repeat: no-repeat; 
        background-position: top; background-size: cover">
    <div class="h-screen min-w-screen">
        <div class="h-1/2 flex">
            <div class="flex self-center mx-auto h-50 w-175 
                rounded-lg border-4 shadow-2xl shadow-white">
                <h1 class="text-center self-center text-4xl text-white font-semibold">
                    A QUOI SONT LIEES LES COULEURS DES FLAMMES ?
                </h1>
            </div>
        </div>
        <div class="h-1/2 flex">
            <div class="self-end mx-auto">
                <button on:click={() => animateScroll.scrollTo({element: '#devpart', duration: 2000})}
                class="h-12 w-20 bg-gray-200 rounded-t-4xl flex hover:bg-gray-400
                transition duration-650"
                style="outline:none;">
                    <div class="self-center mx-auto animate-bounce 
                        hover:animate-none">
                        <svg xmlns="http://www.w3.org/2000/svg" 
                        class="h-6 w-6 hover:stroke-white" fill="none" 
                        viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5">
                            <path stroke-linecap="round" 
                                stroke-linejoin="round" d="M19 13l-7 7-7-7m14-8l-7 7-7-7" />
                        </svg>
                    </div>
                </button>
            </div>
        </div>
    </div>
</div>
<!--I & II-->
<div id="devpart" class="bg-black">
    <div class="min-h-screen min-w-screen bg-black text-white">
        <div class="h-1/2 space-y-5">
            <div class="self-start mx-auto flex justify-center">
                <button on:click={() => animateScroll.scrollTo({element: '#pbq', duration: 2000})}
                class="h-12 w-20 bg-gray-200 rounded-b-4xl flex hover:bg-gray-400
                transition duration-650"
                style="outline:none;">
                    <div class="self-center mx-auto animate-bounce 
                        hover:animate-none">
                        <svg xmlns="http://www.w3.org/2000/svg" 
                        class="h-6 w-6 hover:stroke-white" fill="none" 
                        viewBox="0 0 24 24" stroke="black" stroke-width="1.5">
                            <path stroke-linecap="round" 
                                stroke-linejoin="round" d="M5 11l7-7 7 7M5 19l7-7 7 7" />
                          </svg>
                    </div>
                </button>
            </div>
            <!--I-->
            <div class="space-y-3">
                <div class="flex justify-center font-bold text-3xl space-x-3">
                    <h1>I - Présentation de l'expérience</h1>
                    <button on:click = {show1} style="outline:none">
                        {#if shown1}
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-7 w-7 self-center" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M5 15l7-7 7 7" />
                            </svg>
                        {:else}
                            <svg xmlns="http://www.w3.org/2000/svg" 
                                class="h-7 w-7 self-center" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7" />
                            </svg>
                        {/if}
                    </button>
                </div>
                <ExpExplains bind:shown1 bind:show1>
                    <div class="space-y-3">
                        <div class="flex justify-center font-semibold text-2xl space-x-2">
                            <h1>1 - Le protocole</h1>
                            <button on:click={show11} style="outline:none">
                                {#if shown11}
                                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 self-center" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                                        <path stroke-linecap="round" stroke-linejoin="round" d="M5 15l7-7 7 7" />
                                    </svg>
                                {:else}
                                    <svg xmlns="http://www.w3.org/2000/svg" 
                                        class="h-6 w-6 self-center" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                                        <path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7" />
                                    </svg>
                                {/if}
                            </button>
                        </div>
                        <ExpExplains bind:shown11 bind:show11>
                            <div class="py-3 flex justify-evenly">
                                <img class="rounded-xl w-4/7" src="index-pics/waiting2.png" alt="">
                                <div class="rounded-xl w-2/7 bg-blue-400 px-5 py-5">
                                    Lorem ipsum dolor sit amet consectetur adipisicing elit. Illum veritatis voluptatem explicabo at molestias non necessitatibus. Quis iste qui, accusamus et, rerum officiis accusantium dolorum quia laudantium incidunt dolore necessitatibus.
                                </div>
                            </div>
                        </ExpExplains>
                        <div class="flex justify-center font-semibold text-2xl space-x-2">
                            <h1>2 - Les résultats</h1>
                            <button on:click={show12} style="outline:none">
                                {#if shown12}
                                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 self-center" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                                        <path stroke-linecap="round" stroke-linejoin="round" d="M5 15l7-7 7 7" />
                                    </svg>
                                {:else}
                                    <svg xmlns="http://www.w3.org/2000/svg" 
                                        class="h-6 w-6 self-center" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                                        <path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7" />
                                    </svg>
                                {/if}
                            </button>
                        </div>
                        <ExpExplains bind:shown12 bind:show12>
                            <div class="py-3 flex justify-evenly">
                                <img class="w-2/7 rounded-xl" src="index-pics/waiting.png" alt="">
                                <img class="w-2/7 rounded-xl" src="index-pics/waiting.png" alt="">
                                <img class="w-2/7 rounded-xl" src="index-pics/waiting.png" alt="">
                            </div>
                        </ExpExplains>
                    </div>
                </ExpExplains>
            </div>
            <!--II-->
            <div class="space-y-3">
                <div class="flex justify-center font-bold text-3xl space-x-3">
                    <h1>II - Explications</h1>
                    <button on:click = {show2} style="outline:none">
                        {#if shown2}
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-7 w-7 self-center" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M5 15l7-7 7 7" />
                            </svg>
                        {:else}
                            <svg xmlns="http://www.w3.org/2000/svg" 
                                class="h-7 w-7 self-center" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7" />
                            </svg>
                        {/if}
                    </button>
                </div>
                <ExpExplains bind:shown2 bind:show2>
                    <div class="space-y-3">
                        <div class="flex justify-center font-semibold text-2xl space-x-2">
                            <h1>1 - Les combustibles</h1>
                            <button on:click={show21} style="outline:none">
                                {#if shown21}
                                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 self-center" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                                        <path stroke-linecap="round" stroke-linejoin="round" d="M5 15l7-7 7 7" />
                                    </svg>
                                {:else}
                                    <svg xmlns="http://www.w3.org/2000/svg" 
                                        class="h-6 w-6 self-center" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                                        <path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7" />
                                    </svg>
                                {/if}
                            </button>
                        </div>
                        <ExpExplains bind:shown21 bind:show21>
                            <div class="py-3 flex justify-evenly">
                                <div class="w-2/7 rounded-xl border-3">
                                    <img src="flames/picture7.png" alt="">
                                    <h1 class="flex justify-center">Hamdoullah</h1>
                                </div>
                                <div class="w-2/7 rounded-xl border-3">
                                    <img src="flames/picture6.png" alt="">
                                    <h1 class="flex justify-center">Hamdoullah</h1>
                                </div>
                                <div class="w-2/7 rounded-xl border-3">
                                    <img src="flames/picture5.png" alt="">
                                    <h1 class="flex justify-center">Hamdoullah</h1>
                                </div>
                            </div>
                        </ExpExplains>
                        <div class="flex justify-center font-semibold text-2xl space-x-2">
                            <h1>2 - Le rôle de la température</h1>
                            <button on:click={show22} style="outline:none">
                                {#if shown22}
                                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 self-center" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                                        <path stroke-linecap="round" stroke-linejoin="round" d="M5 15l7-7 7 7" />
                                    </svg>
                                {:else}
                                    <svg xmlns="http://www.w3.org/2000/svg" 
                                        class="h-6 w-6 self-center" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                                        <path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7" />
                                    </svg>
                                {/if}
                            </button>
                        </div>
                        <ExpExplains bind:shown22 bind:show22>
                            <div class="py-3 flex justify-evenly">
                                <img class="h-2/7 rounded-xl border-3" src="index-pics/explained-flame.png" alt="">
                                <div class="h-2/7 w-3/7 space-y-8">
                                    <p class="rounded-xl border-3 py-5 px-5">
                                        Lorem ipsum dolor sit amet consectetur adipisicing elit. Minima iste alias illo asperiores magnam quam 
                                        consequuntur? Quidem nisi delectus voluptatibus vitae aspernatur blanditiis voluptates vel minima, labore 
                                        sapiente sit quos?
                                    </p>
                                    <div class="">
                                        <img class="rounded-xl border-3" src="index-pics/wdue.png" alt="">
                                    </div>
                                </div>
                            </div>
                        </ExpExplains>
                    </div>
                </ExpExplains>
            </div>
        </div>
    </div>
</div>

<!--TODO : CONCLUSION SHIT-->