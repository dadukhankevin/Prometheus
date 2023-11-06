<script>
import Post from '$lib/post.svelte';
import Query from "$lib/query.svelte";
import Choice from "$lib/choice.svelte";
import { onMount } from 'svelte';
import { browser } from '$app/environment';
import 'flowbite';
onMount(async () => {
	get_fact();
});
let response = '';
$: total_facts = [];
async function get_fact() {
	const res = await fetch(`/api/feed?message=history of indian subcontenent`);
	response = await res.text();
	total_facts.push(JSON.parse(response));
	total_facts = total_facts;
}


</script>

<div class="container h-full mx-auto flex justify-center items-center">
	<div class="space-y-10 text-center flex flex-col items-center">
		<h2 class="h2 p-4">Welcome to Prometheus 🔥</h2>
		<div class="flex justify-center space-x-2">
		
		</div>
		<div class="space-y-2 flex flex-col items-center">
			{#each total_facts as fact}
			<Post name={fact.name} post={fact.content}></Post>
			<Choice quiz_question={fact.quiz_question} multiple_choice={fact.multiple_choice}></Choice>
			{/each}
		</div>
	</div>
</div>
