<template>
    <div class="container-lg">
        <div class="row row-cols-3 p-0 m-0 mt-3 blockshow">
            <div class="col-2 logo-left">
                &nbsp;
            </div>
            <div class="col-8">
                <h5 class="text-red text-uppercase p-0 m-1 text-center"></h5>
                <h5 class="text-red text-uppercase p-0 m-0 text-center mt-4 pt-2"><b>O'zbek tili milliy korpusi</b></h5>
                <h5 class="text-red text-uppercase p-0 m-1 text-center"></h5>
            </div>
            <div class="col-2 logo-right">
                &nbsp;
            </div>
        </div>
        <div class="mt-2">
            <nav class="navbar border-style navbar-dark bg-info navbar-expand-lg"><button type="button"
                    aria-label="Toggle navigation" class="navbar-toggler collapsed" aria-expanded="false"
                    aria-controls="nav-text-collapse" style="overflow-anchor: none;"><span
                        class="navbar-toggler-icon"></span></button> <a href="/" class="navbar-brand nuxt-link-active"
                    target="_self">
                    Bosh sahifa
                </a>
                <div id="nav-text-collapse" class="navbar-collapse collapse" style="display: none;">
                    <ul class="navbar-nav">
                        <li class="nav-item b-nav-dropdown dropdown" id="__BVID__17"><a role="button" aria-haspopup="true"
                                aria-expanded="false" href="#" target="_self" class="nav-link dropdown-toggle"
                                id="__BVID__17__BV_toggle_"><span>Loyiha haqida</span></a>
                            <ul tabindex="-1" class="dropdown-menu dropdown-menu-right"
                                aria-labelledby="__BVID__17__BV_toggle_">
                                <div class="card">
                                    <li role="presentation" class="submenyu yangihover1"><a href="/buyurtmachi"
                                            class="dropdown-item" role="menuitem" target="_self">
                                            Buyurtmachi tashkilot
                                        </a></li>
                                    <li role="presentation" class="submenyu yangihover1"><a href="/ijrochi"
                                            class="dropdown-item" role="menuitem" target="_self">
                                            Ijrochi tashkilot
                                        </a></li>
                                    <li role="presentation" class="submenyu yangihover1"><a href="/jamoa"
                                            class="dropdown-item" role="menuitem" target="_self">
                                            Ilmiy jamoa
                                        </a></li>
                                    <li role="presentation" class="submenyu yangihover1"><a href="/nashrlar"
                                            class="dropdown-item" role="menuitem" target="_self">
                                            Nashrlar
                                        </a></li>
                                </div>
                                <div class="card mt-1">
                                    <li role="presentation" class="submenyu yangihover1"><a href="/korpushaqida"
                                            class="dropdown-item" role="menuitem" target="_self">
                                            Korpus haqida
                                        </a></li>
                                    <li role="presentation" class="submenyu yangihover1"><a href="/boshqakorpuslar"
                                            class="dropdown-item" role="menuitem" target="_self">
                                            Boshqa korpuslar
                                        </a></li>
                                </div>
                            </ul>
                        </li>
                        <li class="nav-item"><a href="/lugatlar" aria-current="page"
                                class="nav-link nuxt-link-exact-active nuxt-link-active" target="_self">
                                Lug'at
                            </a></li>
                        <li class="nav-item b-nav-dropdown dropdown" id="__BVID__39"><a role="button" aria-haspopup="true"
                                aria-expanded="false" href="#" target="_self" class="nav-link dropdown-toggle"
                                id="__BVID__39__BV_toggle_"><span>Tilshunoslik tadqiqotlari</span></a>
                            <ul tabindex="-1" class="dropdown-menu dropdown-menu-right"
                                aria-labelledby="__BVID__39__BV_toggle_">
                                <li role="presentation" class="submenyu yangihover1"><a href="/statistiktahlil"
                                        class="dropdown-item" role="menuitem" target="_self">
                                        Statistik tahlil
                                    </a></li>
                                <li role="presentation" class="submenyu yangihover1"><a href="/qidiruv"
                                        class="dropdown-item" role="menuitem" target="_self">
                                        Konkordans
                                    </a></li>
                            </ul>
                        </li>
                        <li class="nav-item"><a href="/yangiliklar" class="nav-link" target="_self">
                                Yangiliklar
                            </a></li>
                        <li class="nav-item"><a href="/boglanish" class="nav-link" target="_self">
                                Bog'lanish
                            </a></li>
                        <li class="nav-item"><a href="#" target="_self" class="nav-link">
                                Matn kiritish
                            </a></li>
                        <li class="nav-item"><a href="#" target="_self" class="nav-link">
                                Akt So'zlar
                        </a></li>
                    </ul>
                </div>
            </nav>
        </div>
        <div class="p-3 background-paper mt-2 vh100">
            <h3 class="text-uppercase text-center text-black-50">
                korpus lug'ati
            </h3>
            <div>
                <form class="form-inline w-100" @submit.prevent="submit">
                    <input v-model="word" type="text"
                        :class="`form-control mb-2 mr-sm-2 inputWidth100 shadow-none ${validation.word ? 'is-invalid' : ''}`"
                        placeholder="So'z kiriting...">
                    <button v-if="loading" type="submit" class="btn btn-success mb-2 buttonWidth" :disabled="loading">
                        <div class="spinner-border spinner-border-sm text-light" role="status">
                            <span class="sr-only">Topilmoqda...</span>
                        </div>
                    </button>
                    <button v-else type="submit" class="btn btn-success mb-2 buttonWidth">
                        Izlash
                    </button>
                </form>
                <small v-if="validation.word" class="text-danger">
                    {{ validation.word }}
                </small>
            </div>
            <div>
                <h3 class="text-warning p-0 m-0 font-weight-bold">
                    <div class="row">
                        <div class="col-md-6">
                            <button class="btn btn-light" @click.prevent="speachVoice">
                                <!-- <img src="../../essets/images/speaker1.png"> -->
                                <img src="/assets/speaker1.png">
                            </button>
                        </div>
                        <div class="col-md-6" />
                    </div>
                </h3>
                <div class="row m-0 p-0 w-100">
                    <div class="col-md-4 border-bottom">
                        <p class="text-black-50 p-0 m-0 font-weight-bold mt-4">
                            Grammatik tavsif:
                        </p>
                    </div>
                    <div class="col-md-8 border-bottom">
                        <p class="text-black-50 p-0 m-0 font-weight-bold mt-4">
                            <span class="blue-text">{{ razmetka }}</span>
                        </p>
                    </div>
                </div>
                <div class="row m-0 p-0">
                    <div class="col-md-4 border-bottom">
                        <p class="text-black-50 p-0 m-0 font-weight-bold mt-4">
                            Lug'aviy shakl:
                        </p>
                    </div>
                    <div class="col-md-8 border-bottom">
                        <p class="text-black-50 p-0 m-0 font-weight-bold mt-4">
                            <span class="blue-text">{{ lemma }}</span>
                        </p>
                    </div>
                </div>
                <div class="row m-0 p-0">
                    <div class="col-md-4 border-bottom">
                        <p class="text-black-50 p-0 m-0 font-weight-bold mt-4">
                            Izoh:
                        </p>
                    </div>
                    <div class="col-md-8 border-bottom">
                        <p class="text-black-50 p-0 m-0 font-weight-bold mt-4">
                            <span class="blue-text izoh" v-html="izoh" />
                        </p>
                    </div>
                </div>
                <!-- <div class="row mt-2">
                    <div class="col-md-12">
                        <div class="mt-5">
                            <div>
                                <button class="btn btn-secondary mb-2">
                                    Imo-ishoralar
                                </button>
                            </div>
                            <div>
                                <span v-for="(figure, index) in figures" :key="index">
                                    <img class="mr-1" :src="`/imo/${figures[index]}.jpg`">
                                </span>
                            </div>
                        </div>
                    </div>
                </div> -->
            </div>
        </div>
        <div class="bg-info mt-2 row qisqa">
            <div class="col-6 card13">
                <p class="p-2 m-0 text-center text-uppercase text-white">
                    O'zbekiston Respublikasi Vazirlar Mahkamasi huzuridagi <br> O'zbek tilini rivojlantirish jamg'armasi
                </p>
            </div>
            <div class="col-6 card13">
                <p class="p-2 m-0 text-center text-uppercase text-white">
                    Muhammad al-Xorazmiy nomidagi <br>Toshkent Axborot Texnologiyalari Universiteti Samarqand filiali
                </p>
            </div>
        </div>
    </div>
</template>
  
<script>
import axios from 'axios'

export default {
    data: () => ({
        word: '',
        title: '',
        lemma: '',
        izoh: '',
        razmetka: '',
        validation: {
            word: ''
        },
        loading: false,
        figures: [],
        items: [],
    }),
    computed: {
        isAuth() {
            return this.$store.getters['auth/isAuth']
        }
    },
    methods: {
        speachVoice() {
            if (this.title !== '') {
                const msg = new SpeechSynthesisUtterance()
                msg.text = this.title
                // console.log('speech', this.title);
                window.speechSynthesis.speak(msg)
            }
        },
        admin() {
            this.$router.push('/admin')
        },
        login() {
            this.$router.push('/login')
        },
        async submit () {
            if(!this.word?.trim()) return
            this.validation.word = ''
            this.loading = true
            // this.figures = this.word.toLowerCase().split('')
            const searched = await axios.get(`https://fair-blue-abalone-garb.cyclic.app//api/words/search/${this.word}`)
            // console.log(searched.data);
            if(searched.data){
                this.title = searched.data.uzbek
                this.lemma = String(searched.data.english).slice(5)
                this.razmetka = String(searched.data.russian).slice(4)
                this.izoh = searched.data.description
            } else {
                this.validation.word = 'Ushbu so\'z topilmadi!'
            }
            
            this.loading = false
        }
    }
}
</script>
  
<style>
@import url('/assets/css.css');

.qisqa {
    margin-left: 0px;
    margin-right: 0px;
}

.card13 {
    /* width: 234px; */
    /* height: 114px; */
    font-size: 14px;
    border-radius: 10px;
    background-color: #39959a50;
    color: #18c8e3;
    box-shadow: 0px 4px 25px 0px rgba(30, 140, 195, 0.362);
    /* transition: all .3s ease-in-out; */
    text-align: center;
}

html,
body {
    background: url('/assets/fon.jpg') repeat;
}

.background-paper {
    background-color: rgba(244, 244, 244, 0.5);
    border-left: 1px solid #b2b2b2;
    border-right: 1px solid #b2b2b2;
}

.blue-text {
    color: #6451a8;
}

.buttonWidth {
    width: 200px;
}

.inputWidth100 {
    min-width: calc(100% - 210px);
}

.vh100 {
    min-height: calc(100vh - 235px);
}

.logo-left {
    background: url('/assets/gerb.png') center center no-repeat;
    background-size: 70%;
    height: 100px;
}

.logo-right {
    background: url('/assets/reg.png') center center no-repeat;
    background-size: 100% 100%;
}

.text-red {
    color: rgb(37, 35, 145);
    font-size: 220%;
}

.border-style {
    border-top-left-radius: 24px;
    border-top-right-radius: 24px;
}

.nav-link {
    color: rgba(255, 255, 255, 0.9) !important;
}

@media only screen and (max-width: 1100px) {
    .blockshow {
        display: none !important;
    }

    .border-style {
        border-top-left-radius: 0px;
        border-top-right-radius: 0px;
    }

    .buttonWidth {
        width: 80px
    }

    .inputWidth100 {
        min-width: calc(100% - 90px);
    }

    .vh100 {
        min-height: calc(100vh - 255px);
    }
}

@media only screen and (max-width: 1300px) {
    h5 {
        font-size: 14pt !important;
    }
}

.yangihover {
    transition: all 0.4s linear;
}

.yangihover:hover {
    transform: scale(1.05);
}

.yangihover1 {
    transition: all 0.3s linear;
}

.yangihover1:hover {
    transform: scale(1.05);
}
</style>
  