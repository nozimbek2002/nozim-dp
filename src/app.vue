<template>
    <div class="bg-purple-50 w-full min-h-screen py-5">
        <div class="container mx-auto">
            <div class="text-center">
                <h1 class="text-purple-600 text-xl uppercase font-medium">AKT So'zlar Bazasi</h1>
            </div>
            <div class="rounded flex gap-2 mt-2">
                <div class="flex-1 rounded-l-2xl overflow-hidden flex items-center pl-4 border-2 border-purple-500 bg-white">
                    <BsSearch />
                    <input v-model="text" placeholder="Lu'gat Izlash" type="text" class="w-full outline-none px-4 py-2">
                </div>
                <button :disabled="!text.trim()" @click="searchItems" class="transition px-8 py-2 text-white bg-purple-600 hover:bg-purple-500 active:bg-purple-400 disabled:bg-purple-900 rounded-r-2xl">Qidirish</button>
            </div>
            <div class="py-2 flex flex-wrap gap-2">
                <div v-for="c,i in categories" :key="i" :value="c" style="display:flex;gap:4px;align-items:center;">
                    <input type="checkbox" hidden v-model="category" :value="c" :id="`c_select_${i}`">
                    <label :for="`c_select_${i}`" class="cursor-pointer px-3 py-0.5 rounded-2xl border-2 border-purple-500 select-none" :class="!!category.find(t => t._id === c._id)?'bg-purple-600 text-white':'text-purple-500'">{{ c.name }}</label>
                </div>
            </div>
            <div class="mt-4 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                
                <div v-for="word,i in results" :key="i" @click="item=i" class="flex flex-col p-6 bg-white rounded-xl border border-transparent transition hover:border-purple-600 hover:shadow cursor-pointer">
                    <h1 class="text-base font-medium">{{word[categories.find(c => c.c_id === word.category)?.mainfield]}}</h1>
                    <p class="flex-1 line-clamp-4 text-sm mt-2">{{ word.description }}</p>
                    <div class="mt-4 flex gap-2 justify-between items-center">
                        <div class="text-xs px-2 py-1 rounded-lg bg-purple-400 text-white">#{{ categories.find(c => c.c_id === word.category)?.name }}</div>
                        <button @click.stop="speechWord(word[categories.find(c => c.c_id === word.category)?.mainfield])" class="text-purple-500 p-3 rounded-full bg-purple-200 hover:bg-purple-100 active:bg-purple-50 cursor-pointer">
                            <FaVolumeHigh />
                        </button>
                    </div>
                </div>

            </div>
        </div>
    </div>

    <div v-if="item!==null" class="fixed z-50 px-4 w-full h-full bg-black/40 top-0 left-0 flex justify-center items-center">
        <div class="bg-white max-w-2xl shadow overflow-hidden rounded-xl">
            <div class="flex justify-between items-center px-6 py-4">
                <h3 class="font-medium text-purple-600 text-lg">So'z haqida umumiy ma'lumot</h3>
                <button @click="item=null" class="text-red-500"><ClCloseLg/></button>
            </div>
            <div class="border-t border-gray-200">
                <dl>
                    <div v-for="c,i in category.find(c => c.c_id == results[item].category)?.fields||[]" :key="i" class="bg-white px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                        <dt class="text-sm font-medium text-purple-600">
                            {{ c.placeholder }}
                        </dt>
                        <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
                            {{ results?.[item]?.[c.name] }}
                        </dd>
                    </div>

                    <div class="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                        <dt class="text-sm font-medium text-purple-600">
                            Izoh
                        </dt>
                        <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
                            {{ results?.[item]?.description }}
                        </dd>
                    </div>
                </dl>
            </div>
        </div>
    </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { BsSearch, ClCloseLg, FaVolumeHigh } from '@kalimahapps/vue-icons'

const text = ref('')
const item = ref(null)
const loading = ref(false)
const results = ref([])
const category = ref([])
const categories = ref([])

const url = 'http://localhost:5000'

const searchItems = async () => {
    try {
        loading.value = true
        const { data } = await axios.get(`${url}/api/words/search/${text.value}?fields=${category.value.reduce((a,b) => a +','+ b.mainfield,'')}`)
        if(data){
            results.value = data
        } else {
            alert("Ushbu so'z topilmadi")
        }
    } catch (error) {
        console.log(error);
    } finally {
        loading.value = false
    }
}

const get_words = async () => {
    try {
        loading.value = true
        const { data } = await axios.get(`${url}/api/words?search=&page=1&perpage=12&category=${category.value[0].c_id}`)
        if(data){
            results.value = data.result
        } else {
            alert("Ushbu so'z topilmadi")
        }
    } catch (error) {
        console.log(data);
    } finally {
        loading.value = false
    }
}

const speechWord = (word) => {
    const msg = new SpeechSynthesisUtterance()
    msg.text = word
    window.speechSynthesis.speak(msg)
}

const get_categories = async () => {
    try {
        const { data } = await axios.get(`${url}/api/categories?page=1&limit=1000`)
        categories.value = data.result
        if(data.result[0]) {
            category.value.push(data.result[0])
            get_words()
        }
    } catch (error) {
        console.log(data);
    }
}

get_categories()
</script>