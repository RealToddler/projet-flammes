<script lang="js">
    const folks = [
        {name: "ROBERT Maxime", url: "maxime_pfp.png"},
        {name: "DEFONTAINE JOLIVET Emilien", url: "emilien_pfp.png", easter_egg: "https://c.tenor.com/wTKt4BjN7TsAAAAd/zant-just-got-rick-rolled-zant.gif"},
        {name: "PAVESIS Lucas", url: "lucas_pfp.png"}
    ];
</script>

<div class="min-h-80 min-w-screen 
    bg-cyan-900">
    <div class="
        flex justify-center py-7 
        text-white">
        <h1 class="
            text-4xl text-center
            font-bold">
            PROJET REALISE PAR
        </h1>
    </div>
    <div>
        <ul class="
            flex justify-center self-center
            text-white text-2xl 
            font-semibold
            ">
            {#each folks as folk}
                <li class="w-2/9">
                    <div class="h-160px w-160px
                        mx-auto self-center
                        rounded-full border-2 border-white"
                    style="background-image: url({folk.url}); 
                        background-repeat: no-repeat; 
                        background-position: center; 
                        background-size: cover">
                    </div>
                {#if folk.easter_egg}
                    <a href="{folk.easter_egg}">
                        <h1 class="flex justify-center py-3">
                            {folk.name}
                        </h1>
                    </a>
                {:else}
                    <h1 class="flex justify-center py-3">
                        {folk.name}
                    </h1>
                {/if}
                </li>    
            {/each}
        </ul>  
    </div>
</div>