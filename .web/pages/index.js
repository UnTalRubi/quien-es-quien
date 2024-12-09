/** @jsxImportSource @emotion/react */


import { ErrorBoundary } from "react-error-boundary"
import { Fragment, useCallback, useContext, useEffect, useState } from "react"
import { ColorModeContext, EventLoopContext, StateContexts } from "$/utils/context"
import { Event, getBackendURL, getRefValue, getRefValues, isTrue, refs } from "$/utils/state"
import { jsx, keyframes } from "@emotion/react"
import { WifiOffIcon as LucideWifiOffIcon } from "lucide-react"
import { toast, Toaster } from "sonner"
import env from "$/env.json"
import { Box as RadixThemesBox, Button as RadixThemesButton, Card as RadixThemesCard, Code as RadixThemesCode, Flex as RadixThemesFlex, Grid as RadixThemesGrid, Heading as RadixThemesHeading, Inset as RadixThemesInset, Link as RadixThemesLink, Text as RadixThemesText, TextField as RadixThemesTextField } from "@radix-ui/themes"
import { Root as RadixFormRoot } from "@radix-ui/react-form"
import { DebounceInput } from "react-debounce-input"
import ReactMarkdown from "react-markdown"
import "katex/dist/katex.min.css"
import remarkMath from "remark-math"
import remarkGfm from "remark-gfm"
import remarkUnwrapImages from "remark-unwrap-images"
import rehypeKatex from "rehype-katex"
import rehypeRaw from "rehype-raw"
import NextLink from "next/link"
import { PrismAsyncLight as SyntaxHighlighter } from "react-syntax-highlighter"
import oneDark from "react-syntax-highlighter/dist/cjs/styles/prism/one-dark"
import oneLight from "react-syntax-highlighter/dist/cjs/styles/prism/one-light"
import NextHead from "next/head"



export function Fragment_9017984ada32ffa55f5d2870ebd3c887 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);



  return (
    <Fragment>

{isTrue((connectErrors.length > 0)) ? (
  <Fragment>

<LucideWifiOffIcon css={({ ["color"] : "crimson", ["zIndex"] : 9999, ["position"] : "fixed", ["bottom"] : "33px", ["right"] : "33px", ["animation"] : (pulse+" 1s infinite") })} size={32}/>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
  )
}

export function Debounceinput_5b8f0dd0ccb5bb5b02897414646dd31a () {
  const reflex___state____state__quien_es_quien___state____state = useContext(StateContexts.reflex___state____state__quien_es_quien___state____state)
  const [addEvents, connectErrors] = useContext(EventLoopContext);

  const on_change_831b4dff78310f724a7ebfe170e437bf = useCallback(((_e) => (addEvents([(Event("reflex___state____state.quien_es_quien___state____state.set_pregunta", ({ ["value"] : _e["target"]["value"] }), ({  })))], [_e], ({  })))), [addEvents, Event])


  return (
    <DebounceInput css={({ ["width"] : "100%" })} debounceTimeout={300} element={RadixThemesTextField.Root} onChange={on_change_831b4dff78310f724a7ebfe170e437bf} placeholder={"Introduce una caracter\u00edstica"} type={"text"} value={reflex___state____state__quien_es_quien___state____state.pregunta}/>
  )
}

export function Button_cd6c5ff65c8eddf2906fe404076b34a5 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

  const on_click_67a16e8a141ccb428cec3c37d0b07ad3 = useCallback(((...args) => (addEvents([(Event("reflex___state____state.quien_es_quien___state____state.obtener_caracteristicas", ({  }), ({  }))), (Event("reflex___state____state.quien_es_quien___state____state.mensaje_adivinar", ({  }), ({  }))), (Event("reflex___state____state.quien_es_quien___state____state.comprobacion", ({  }), ({  })))], args, ({  })))), [addEvents, Event])


  return (
    <RadixThemesButton css={({ ["&:hover"] : null })} onClick={on_click_67a16e8a141ccb428cec3c37d0b07ad3} type={"submit"}>

{"Preguntar"}
</RadixThemesButton>
  )
}

export function Toaster_6e6ebf8d7ce589d59b7d382fb7576edf () {
  const { resolvedColorMode } = useContext(ColorModeContext)


  refs['__toast'] = toast
  const [addEvents, connectErrors] = useContext(EventLoopContext);
  const toast_props = ({ ["description"] : ("Check if server is reachable at "+getBackendURL(env.EVENT).href), ["closeButton"] : true, ["duration"] : 120000, ["id"] : "websocket-error" });
  const [userDismissed, setUserDismissed] = useState(false);
  (useEffect(
() => {
    if ((connectErrors.length >= 2)) {
        if (!userDismissed) {
            toast.error(
                `Cannot connect to server: ${((connectErrors.length > 0) ? connectErrors[connectErrors.length - 1].message : '')}.`,
                {...toast_props, onDismiss: () => setUserDismissed(true)},
            )
        }
    } else {
        toast.dismiss("websocket-error");
        setUserDismissed(false);  // after reconnection reset dismissed state
    }
}
, [connectErrors]))

  return (
    <Toaster closeButton={false} expand={true} position={"bottom-right"} richColors={true} theme={resolvedColorMode}/>
  )
}

export function Root_579135acee735bb4355ab7a6c6c36883 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);


  
    const handleSubmit_2d43c82fe445cfc0b49f5c89ddfc9d22 = useCallback((ev) => {
        const $form = ev.target
        ev.preventDefault()
        const form_data = {...Object.fromEntries(new FormData($form).entries()), ...({  })};

        (((...args) => (addEvents([(Event("reflex___state____state.quien_es_quien___state____state.obtener_caracteristicas", ({  }), ({  }))), (Event("reflex___state____state.quien_es_quien___state____state.mensaje_adivinar", ({  }), ({  }))), (Event("reflex___state____state.quien_es_quien___state____state.comprobacion", ({  }), ({  })))], args, ({  }))))());

        if (true) {
            $form.reset()
        }
    })
    

  return (
    <RadixFormRoot className={"Root "} css={({ ["width"] : "20em" })} onSubmit={handleSubmit_2d43c82fe445cfc0b49f5c89ddfc9d22}>

<Debounceinput_5b8f0dd0ccb5bb5b02897414646dd31a/>
</RadixFormRoot>
  )
}

export function Button_a06f6af7edfc5f0e49f2cfc141dc03be () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

  const on_click_8d563b72e1e2474c21c862a74561bbfd = useCallback(((...args) => (addEvents([(Event("reflex___state____state.quien_es_quien___state____state.reiniciar_partida", ({  }), ({  })))], args, ({  })))), [addEvents, Event])


  return (
    <RadixThemesButton css={({ ["font-size"] : "20px", ["padding"] : "30px 30px", ["margin-left"] : "57em", ["&:hover"] : null })} onClick={on_click_8d563b72e1e2474c21c862a74561bbfd}>

{"Reiniciar partida"}
</RadixThemesButton>
  )
}

export function Errorboundary_4b8352435d32d0ae149cfaf9228ff69b () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

  const on_error_0f5dbf674521530422d73a7946faf6d4 = useCallback(((_error, _info) => (addEvents([(Event("reflex___state____state.reflex___state____frontend_event_exception_state.handle_frontend_exception", ({ ["stack"] : _error["stack"], ["component_stack"] : _info["componentStack"] }), ({  })))], [_error, _info], ({  })))), [addEvents, Event])


  return (
    <ErrorBoundary fallbackRender={((event_args) => (jsx("div", ({ ["css"] : ({ ["height"] : "100%", ["width"] : "100%", ["position"] : "absolute", ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center" }) }), (jsx("div", ({ ["css"] : ({ ["display"] : "flex", ["flexDirection"] : "column", ["gap"] : "1rem" }) }), (jsx("div", ({ ["css"] : ({ ["display"] : "flex", ["flexDirection"] : "column", ["gap"] : "1rem", ["maxWidth"] : "50ch", ["border"] : "1px solid #888888", ["borderRadius"] : "0.25rem", ["padding"] : "1rem" }) }), (jsx("h2", ({ ["css"] : ({ ["fontSize"] : "1.25rem", ["fontWeight"] : "bold" }) }), (jsx(Fragment, ({  }), "An error occurred while rendering this page.")))), (jsx("p", ({ ["css"] : ({ ["opacity"] : "0.75" }) }), (jsx(Fragment, ({  }), "This is an error with the application itself.")))), (jsx("details", ({  }), (jsx("summary", ({ ["css"] : ({ ["padding"] : "0.5rem" }) }), (jsx(Fragment, ({  }), "Error message")))), (jsx("div", ({ ["css"] : ({ ["width"] : "100%", ["maxHeight"] : "50vh", ["overflow"] : "auto", ["background"] : "#000", ["color"] : "#fff", ["borderRadius"] : "0.25rem" }) }), (jsx("div", ({ ["css"] : ({ ["padding"] : "0.5rem", ["width"] : "fit-content" }) }), (jsx("pre", ({  }), (jsx(Fragment, ({  }), event_args.error.stack)))))))), (jsx("button", ({ ["css"] : ({ ["padding"] : "0.35rem 0.75rem", ["margin"] : "0.5rem", ["background"] : "#fff", ["color"] : "#000", ["border"] : "1px solid #000", ["borderRadius"] : "0.25rem", ["fontWeight"] : "bold" }), ["onClick"] : ((...args) => (addEvents([(Event("_call_function", ({ ["function"] : (() => (navigator["clipboard"]["writeText"](event_args.error.stack))) }), ({  })))], args, ({  })))) }), (jsx(Fragment, ({  }), "Copy")))))))), (jsx("hr", ({ ["css"] : ({ ["borderColor"] : "currentColor", ["opacity"] : "0.25" }) }))), (jsx("a", ({ ["href"] : "https://reflex.dev" }), (jsx("div", ({ ["css"] : ({ ["display"] : "flex", ["alignItems"] : "baseline", ["justifyContent"] : "center", ["fontFamily"] : "monospace", ["--default-font-family"] : "monospace", ["gap"] : "0.5rem" }) }), (jsx(Fragment, ({  }), "Built with ")), (jsx("svg", ({ ["css"] : ({ ["viewBox"] : "0 0 56 12", ["fill"] : "currentColor" }), ["height"] : "12", ["width"] : "56", ["xmlns"] : "http://www.w3.org/2000/svg" }), (jsx("path", ({ ["d"] : "M0 11.5999V0.399902H8.96V4.8799H6.72V2.6399H2.24V4.8799H6.72V7.1199H2.24V11.5999H0ZM6.72 11.5999V7.1199H8.96V11.5999H6.72Z" }))), (jsx("path", ({ ["d"] : "M11.2 11.5999V0.399902H17.92V2.6399H13.44V4.8799H17.92V7.1199H13.44V9.3599H17.92V11.5999H11.2Z" }))), (jsx("path", ({ ["d"] : "M20.16 11.5999V0.399902H26.88V2.6399H22.4V4.8799H26.88V7.1199H22.4V11.5999H20.16Z" }))), (jsx("path", ({ ["d"] : "M29.12 11.5999V0.399902H31.36V9.3599H35.84V11.5999H29.12Z" }))), (jsx("path", ({ ["d"] : "M38.08 11.5999V0.399902H44.8V2.6399H40.32V4.8799H44.8V7.1199H40.32V9.3599H44.8V11.5999H38.08Z" }))), (jsx("path", ({ ["d"] : "M47.04 4.8799V0.399902H49.28V4.8799H47.04ZM53.76 4.8799V0.399902H56V4.8799H53.76ZM49.28 7.1199V4.8799H53.76V7.1199H49.28ZM47.04 11.5999V7.1199H49.28V11.5999H47.04ZM53.76 11.5999V7.1199H56V11.5999H53.76Z" }))))))))))))))} onError={on_error_0f5dbf674521530422d73a7946faf6d4}>

<Fragment>

<Div_bd4c022a8f796682aa6392e9d4c102e9/>
<Toaster_6e6ebf8d7ce589d59b7d382fb7576edf/>
</Fragment>
<RadixThemesFlex align={"center"} className={"rx-Stack"} direction={"column"} gap={"3"}>

<RadixThemesHeading as={"h1"} css={({ ["margin"] : "1em" })} size={"8"}>

{"\u00bfQui\u00e9n es Qui\u00e9n?"}
</RadixThemesHeading>
<RadixThemesBox>

<Text_9d09bd61400cbb12d3095abf0c147daf/>
</RadixThemesBox>
<RadixThemesFlex align={"center"} className={"rx-Stack"} direction={"row"} gap={"3"}>

<Grid_e5c8fb6bd1de16f807a79a7fc8410548/>
<RadixThemesCard css={({ ["height"] : "17em", ["width"] : "10em", ["marginLeft"] : "5em" })}>

<RadixThemesInset>

<Fragment_839aeecc01e644b4e21157cc8e4807cd/>
</RadixThemesInset>
</RadixThemesCard>
</RadixThemesFlex>
<RadixThemesHeading css={({ ["fontSize"] : "2em" })}>

{"Tu personaje es aa secreto "}
</RadixThemesHeading>
<RadixThemesFlex align={"start"} className={"rx-Stack"} direction={"row"} gap={"3"}>

<Button_a06f6af7edfc5f0e49f2cfc141dc03be/>
</RadixThemesFlex>
<RadixThemesFlex align={"start"} className={"rx-Stack"} direction={"row"} gap={"3"}>

<Root_579135acee735bb4355ab7a6c6c36883/>
<Button_cd6c5ff65c8eddf2906fe404076b34a5/>
</RadixThemesFlex>
<RadixThemesBox>

<ReactMarkdown components={ComponentMap_a42fc60f349fa409e8dc777ee7e776ff()} rehypePlugins={[rehypeKatex, rehypeRaw]} remarkPlugins={[remarkMath, remarkGfm, remarkUnwrapImages]}>

{"### Checkea este proyecto en [Github](https://github.com/UnTalRubi/quien-es-quien)"}
</ReactMarkdown>
</RadixThemesBox>
</RadixThemesFlex>
<NextHead>

<title>

{"QuienEsQuien | Index"}
</title>
<meta content={"favicon.ico"} property={"og:image"}/>
</NextHead>
</ErrorBoundary>
  )
}

export function Text_9d09bd61400cbb12d3095abf0c147daf () {
  const reflex___state____state__quien_es_quien___state____state = useContext(StateContexts.reflex___state____state__quien_es_quien___state____state)



  return (
    <RadixThemesText as={"p"} size={"7"}>

{reflex___state____state__quien_es_quien___state____state.texto_puntuacion}
</RadixThemesText>
  )
}

const pulse = keyframes`
    0% {
        opacity: 0;
    }
    100% {
        opacity: 1;
    }
`


export function Fragment_839aeecc01e644b4e21157cc8e4807cd () {
  const reflex___state____state__quien_es_quien___state____state = useContext(StateContexts.reflex___state____state__quien_es_quien___state____state)



  return (
    <Fragment>

{isTrue(reflex___state____state__quien_es_quien___state____state.mostrar_resultado) ? (
  <Fragment>

<img css={({ ["width"] : "100%", ["height"] : "auto" })} src={(reflex___state____state__quien_es_quien___state____state.personaje_jugador+".jpg")}/>
</Fragment>
) : (
  <Fragment>

{isTrue(!(reflex___state____state__quien_es_quien___state____state.mostrar_resultado)) ? (
  <Fragment>

<img css={({ ["width"] : "100%", ["height"] : "auto" })} src={"ocultar.png"}/>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
)}
</Fragment>
  )
}

        function ComponentMap_a42fc60f349fa409e8dc777ee7e776ff () {
            const { resolvedColorMode } = useContext(ColorModeContext)
const _language = "python"

 if (_language) {
    (async () => {
      try {
        const module = await import(`react-syntax-highlighter/dist/cjs/languages/prism/${_language}`);
        SyntaxHighlighter.registerLanguage(_language, module.default);
      } catch (error) {
        console.error(`Error importing language module for ${_language}:`, error);
      }
    })();
  }

            return (
                ({ ["h1"] : (({node, children, ...props}) => (<RadixThemesHeading as={"h1"} css={({ ["marginTop"] : "0.5em", ["marginBottom"] : "0.5em" })} size={"6"} {...props}>{children}</RadixThemesHeading>)), ["h2"] : (({node, children, ...props}) => (<RadixThemesHeading as={"h2"} css={({ ["marginTop"] : "0.5em", ["marginBottom"] : "0.5em" })} size={"5"} {...props}>{children}</RadixThemesHeading>)), ["h3"] : (({node, children, ...props}) => (<RadixThemesHeading as={"h3"} css={({ ["marginTop"] : "0.5em", ["marginBottom"] : "0.5em" })} size={"4"} {...props}>{children}</RadixThemesHeading>)), ["h4"] : (({node, children, ...props}) => (<RadixThemesHeading as={"h4"} css={({ ["marginTop"] : "0.5em", ["marginBottom"] : "0.5em" })} size={"3"} {...props}>{children}</RadixThemesHeading>)), ["h5"] : (({node, children, ...props}) => (<RadixThemesHeading as={"h5"} css={({ ["marginTop"] : "0.5em", ["marginBottom"] : "0.5em" })} size={"2"} {...props}>{children}</RadixThemesHeading>)), ["h6"] : (({node, children, ...props}) => (<RadixThemesHeading as={"h6"} css={({ ["marginTop"] : "0.5em", ["marginBottom"] : "0.5em" })} size={"1"} {...props}>{children}</RadixThemesHeading>)), ["p"] : (({node, children, ...props}) => (<RadixThemesText as={"p"} css={({ ["marginTop"] : "1em", ["marginBottom"] : "1em" })} {...props}>{children}</RadixThemesText>)), ["ul"] : (({node, children, ...props}) => (<ul css={({ ["listStyleType"] : "disc", ["marginTop"] : "1em", ["marginBottom"] : "1em", ["marginLeft"] : "1.5rem", ["direction"] : "column" })}>{children}</ul>)), ["ol"] : (({node, children, ...props}) => (<ol css={({ ["listStyleType"] : "decimal", ["marginTop"] : "1em", ["marginBottom"] : "1em", ["marginLeft"] : "1.5rem", ["direction"] : "column" })}>{children}</ol>)), ["li"] : (({node, children, ...props}) => (<li css={({ ["marginTop"] : "0.5em", ["marginBottom"] : "0.5em" })}>{children}</li>)), ["a"] : (({node, children, ...props}) => (<RadixThemesLink css={({ ["&:hover"] : ({ ["color"] : "var(--accent-8)" }) })} {...props}>{children}</RadixThemesLink>)), ["code"] : (({node, inline, className, children, ...props}) => { const match = (className || '').match(/language-(?<lang>.*)/); const _language = match ? match[1] : '';   if (_language) {     (async () => {       try {         const module = await import(`react-syntax-highlighter/dist/cjs/languages/prism/${_language}`);         SyntaxHighlighter.registerLanguage(_language, module.default);       } catch (error) {         console.error(`Error importing language module for ${_language}:`, error);       }     })();   }  ;             return inline ? (                 <RadixThemesCode {...props}>{children}</RadixThemesCode>             ) : (                 <SyntaxHighlighter children={((Array.isArray(children)) ? children.join("\n") : children)} css={({ ["marginTop"] : "1em", ["marginBottom"] : "1em" })} customStyle={({ ["marginTop"] : "1em", ["marginBottom"] : "1em" })} language={_language} style={((resolvedColorMode === "light") ? oneLight : oneDark)} wrapLongLines={true} {...props}/>             );         }) })
            )
        }
        

export function Div_bd4c022a8f796682aa6392e9d4c102e9 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);



  return (
    <div css={({ ["position"] : "fixed", ["width"] : "100vw", ["height"] : "0" })} title={("Connection Error: "+((connectErrors.length > 0) ? connectErrors[connectErrors.length - 1].message : ''))}>

<Fragment_9017984ada32ffa55f5d2870ebd3c887/>
</div>
  )
}

export function Grid_e5c8fb6bd1de16f807a79a7fc8410548 () {
  const reflex___state____state__quien_es_quien___state____state = useContext(StateContexts.reflex___state____state__quien_es_quien___state____state)



  return (
    <RadixThemesGrid columns={"8"} rows={"3"} gap={"3"}>

<>{["Susan", "Claire", "David", "Anne", "Robert", "Anita", "Joe", "George", "Bill", "Alfred", "Max", "Tom", "Alex", "Sam", "Richard", "Paul", "Maria", "Frans", "Herman", "Bernard", "Philip", "Eric", "Charles", "Peter"].map((nombre, index_9fdc9f8de27ce0f4) => (
  <RadixThemesCard css={({ ["height"] : "12em", ["width"] : "7.5em", ["border"] : "0px" })} key={index_9fdc9f8de27ce0f4}>

<RadixThemesInset>

<Fragment>

{isTrue(reflex___state____state__quien_es_quien___state____state.personajes_tumbados.includes(nombre)) ? (
  <Fragment>

<img css={({ ["width"] : "100%", ["height"] : "auto" })} src={"ocultar.png"}/>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
<Fragment>

{isTrue(!(reflex___state____state__quien_es_quien___state____state.personajes_tumbados.includes(nombre))) ? (
  <Fragment>

<img css={({ ["width"] : "100%", ["height"] : "auto" })} src={(nombre+".jpg")}/>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
</RadixThemesInset>
</RadixThemesCard>
))}</>
</RadixThemesGrid>
  )
}

export default function Component() {

  return (
    <Errorboundary_4b8352435d32d0ae149cfaf9228ff69b/>
  )
}
