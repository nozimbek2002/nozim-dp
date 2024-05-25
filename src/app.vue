<template>
    <div class="bg-purple-50 w-full min-h-screen">
        <div class="flex flex-col md:flex-row w-full">
            <div class="max-w-full md:max-w-[350px] h-min md:h-screen p-4 w-full bg-white flex flex-col">
                <div class="rounded flex gap-2 mt-2">
                    <div class="flex-1 rounded-lg overflow-hidden flex items-center border-2 border-purple-500 bg-white">
                        <input v-model="text" @input="searchItems" placeholder="Lu'gat Izlash" type="text" class="w-full outline-none px-4 py-1.5">
                    </div>
                    <button type="button" @click="filter=!filter" class="transition px-3 py-1 text-white bg-purple-600 hover:bg-purple-500 active:bg-purple-400 disabled:bg-purple-900 rounded-lg">
                        <SuFiltering />
                    </button>
                </div>
                <div class="py-3 flex flex-wrap gap-2" v-show="filter">
                    <div v-for="c,i in categories" :key="i" :value="c" style="display:flex;gap:4px;align-items:center;">
                        <input type="checkbox" hidden v-model="category" :value="c" :id="`c_select_${i}`">
                        <label :for="`c_select_${i}`" class="cursor-pointer text-sm px-2 py-0.5 rounded-3xl border-2 border-purple-500 select-none" :class="!!category.find(t => t._id === c._id)?'bg-purple-600 text-white':'text-purple-500'">{{ c.name }}</label>
                    </div>
                </div>
                
                <div class="hidden md:block border-t border-gray-200">
                    <dl v-if="item!==null" class="mt-2">
                        <div v-for="c,i in categories.find(c => c.c_id == results?.[item]?.category)?.fields||[]" :key="i" class="bg-white p-4">
                            <dt class="text-sm font-medium text-purple-600">
                                {{ c.placeholder }}
                            </dt>
                            <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
                                {{ results?.[item]?.[c.name] }}
                            </dd>
                        </div>

                        <div class="bg-gray-50 rounded-lg p-4">
                            <dt class="text-sm font-medium text-purple-600">
                                Izoh
                            </dt>
                            <dd class="mt-2 text-sm text-gray-900">
                                {{ results?.[item]?.description }}
                            </dd>
                        </div>
                    </dl>
                </div>

            </div>

            <div v-if="loading" class="flex-1 h-screen flex items-center justify-center">
                <div class="animate-spin">
                    <McLoading2Line class="w-10 h-10 text-purple-600" />
                </div>
            </div>

            <div v-else class="flex-1 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 p-4 max-h-screen overflow-auto" style="grid-template-rows: min-content;">
                <div v-for="word,i in results" :key="i" @click="item=i" class="max-h-[220px] h-min flex flex-col p-6 bg-white rounded-xl border border-transparent transition hover:border-purple-600 hover:shadow cursor-pointer" :class="{'bg-gray-100 border-purple-600': i === item}">
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

    <div v-if="item!==null" class="fixed z-50 px-4 w-full h-full bg-black/40 top-0 left-0 flex md:hidden justify-center items-center">
        <div class="bg-white max-w-2xl shadow overflow-hidden rounded-xl">
            <div class="flex justify-between items-center px-6 py-4">
                <h3 class="font-medium text-purple-600 text-lg">So'z haqida umumiy ma'lumot</h3>
                <button @click="item=null" class="text-red-500"><ClCloseLg/></button>
            </div>
            <div class="border-t border-gray-200">
                <dl>
                    <div v-for="c,i in category.find(c => c.c_id == results[item].category)?.fields||[]" :key="i" class="bg-white py-5 sm:grid sm:grid-cols-3 px-6">
                        <dt class="text-sm font-medium text-purple-600">
                            {{ c.placeholder }}
                        </dt>
                        <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
                            {{ results?.[item]?.[c.name] }}
                        </dd>
                    </div>

                    <div class="bg-gray-50 py-5 sm:grid sm:grid-cols-3 px-6">
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
import lodash from 'lodash'
import { ref, watch } from 'vue'
import { McLoading2Line, FaVolumeHigh, ClCloseLg, SuFiltering } from '@kalimahapps/vue-icons'

const text = ref('')
const item = ref(null)
const loading = ref(true)
const filter = ref(false)
const results = ref([])
const category = ref([])
const categories = ref([])

const url = 'https://fair-blue-abalone-garb.cyclic.app'

const searchItems = lodash.debounce(async () => {
    try {
        if(!text.value.trim()) return get_words()
        item.value = null
        loading.value = true
        const { data } = await axios.get(`${url}/api/words/search/${text.value}?fields=${category.value.reduce((a,b) => a +','+ b.mainfield,'')}`)
        if(data){
            results.value = data
        } else {
            alert("Ushbu so'z topilmadi")
        }
    } catch (error) {
        console.log(error)
    } finally {
        loading.value = false
    }
}, 500)

const get_words = async () => {
    try {
        item.value = null
        loading.value = true
        const { data } = await axios.get(`${url}/api/words?search=&page=1&perpage=96&category=${category.value[0].c_id}`)
        if(data){
            results.value = data.result
        } else {
            alert("Ushbu so'z topilmadi")
        }
    } catch (error) {
        console.log(data)
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
        }
    } catch (error) {
        console.log(error);
    }
}

watch(category, () => get_words(), { deep: true })

get_categories()
</script>