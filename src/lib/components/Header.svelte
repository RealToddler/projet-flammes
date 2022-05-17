<script lang="js">
    const menus = [
        {title: "GALERIE", href: "gallery"}, 
        {title: "PAGE D'ACCUEIL", href: ''}, 
        {title: "RESSOURCES", href: "ressources"}
        ];
</script>

<div class="h-25 w-screen
    flex justify-center 
    bg-cyan-900">
    <ul class="w-full 
        flex justify-evenly self-center
        text-white text-3xl 
        font-semibold">
        {#each menus as menu}
            <li>
                <a href="/{menu.href}" 
                class="summary hover:text-rose-500 transition duration-650">
                    {menu.title} 
                </a>
            </li>
        {/each}
    </ul>
</div>
