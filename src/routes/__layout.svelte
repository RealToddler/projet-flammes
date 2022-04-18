<script lang="ts">
    import Header from "$lib/components/Header.svelte"
    import Footer from "$lib/components/Footer.svelte"
</script>   

<header>
    <Header />
</header>
<body>
    <slot></slot>
</body>
<footer>
    <Footer />
</footer>

<style windi:preflights:global windi:safelist:global>
</style>